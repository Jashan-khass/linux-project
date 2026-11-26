
import psutil


def get_process_info():

    print("\nRUNNING PROCESSES")

    processes = []

    for process in psutil.process_iter(
        ["pid", "name", "username", "memory_percent"]
    ):

        try:
            info = process.info

            processes.append({
                "pid": info["pid"],
                "name": info["name"],
                "username": info["username"],
                "memory": info["memory_percent"] or 0
            })

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    # Sort processes by RAM usage
    processes.sort(
        key=lambda process: process["memory"],
        reverse=True
    )

    print(f"\n{'PID':<10} {'NAME':<25} {'USER':<15} {'RAM %':<10}")
    print("-" * 65)

    for process in processes[:15]:

        print(
            f"{process['pid']:<10} "
            f"{str(process['name'])[:24]:<25} "
            f"{str(process['username'])[:14]:<15} "
            f"{process['memory']:.2f}%"
        )

    print("\nShowing top 15 processes by RAM usage.")


if __name__ == "__main__":
    get_process_info()
