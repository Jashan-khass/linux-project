
import psutil


def get_process_info():

    print("\nRUNNING PROCESSES")

    processes = []

    for process in psutil.process_iter(
        ["pid", "name", "username", "memory_percent"]
    ):

        try:
            # Measure CPU usage
            cpu_usage = process.cpu_percent(interval=None)

            info = process.info

            processes.append({
                "pid": info["pid"],
                "name": info["name"],
                "username": info["username"],
                "memory": info["memory_percent"] or 0,
                "cpu": cpu_usage
            })

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    # Sort processes by CPU usage
    processes.sort(
        key=lambda process: process["cpu"],
        reverse=True
    )

    print(
        f"\n{'PID':<8} {'NAME':<22} "
        f"{'CPU %':<10} {'RAM %':<10}"
    )
    print("-" * 55)

    for process in processes[:15]:

        print(
            f"{process['pid']:<8} "
            f"{str(process['name'])[:21]:<22} "
            f"{process['cpu']:<10.2f} "
            f"{process['memory']:<10.2f}"
        )

    print("\nShowing top 15 processes by CPU usage.")


if __name__ == "__main__":
    get_process_info()
