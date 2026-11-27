
import psutil
import time


def get_process_info():

    print("\nRUNNING PROCESSES")

    processes = []

    # First CPU measurement
    for process in psutil.process_iter():

        try:
            process.cpu_percent(interval=None)
            processes.append(process)

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    # Wait for second CPU measurement
    time.sleep(1)

    results = []

    for process in processes:

        try:
            info = process.as_dict(
                attrs=["pid", "name", "username", "memory_percent"]
            )

            cpu_usage = process.cpu_percent(interval=None)

            results.append({
                "pid": info["pid"],
                "name": info["name"],
                "username": info["username"],
                "memory": info["memory_percent"] or 0,
                "cpu": cpu_usage
            })

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    # Sort by CPU usage
    results.sort(
        key=lambda item: item["cpu"],
        reverse=True
    )

    print(
        f"\n{'PID':<8} {'NAME':<22} "
        f"{'CPU %':<10} {'RAM %':<10}"
    )
    print("-" * 55)

    for process in results[:15]:

        print(
            f"{process['pid']:<8} "
            f"{str(process['name'])[:21]:<22} "
            f"{process['cpu']:<10.2f} "
            f"{process['memory']:<10.2f}"
        )

    print("\nShowing top 15 processes by CPU usage.")


if __name__ == "__main__":
    get_process_info()


def get_process_data():
    import psutil

    process_list = []

    for process in psutil.process_iter(
        attrs=["pid", "name", "username", "memory_percent"]
    ):
        try:
            data = process.info

            process_list.append({
                "pid": data["pid"],
                "name": data["name"],
                "username": data["username"],
                "memory": data["memory_percent"]
            })

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    # Sort processes by RAM usage
    process_list.sort(
        key=lambda x: x["memory"] or 0,
        reverse=True
    )

    return process_list[:15]
