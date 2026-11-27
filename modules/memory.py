
import psutil

def get_memory_info():
    memory = psutil.virtual_memory()

    print("\nRAM INFORMATION")
    print(f"Total RAM: {memory.total / (1024 ** 3):.2f} GB")
    print(f"Used RAM: {memory.used / (1024 ** 3):.2f} GB")
    print(f"Available RAM: {memory.available / (1024 ** 3):.2f} GB")
    print(f"RAM Usage: {memory.percent}%")

    if memory.percent < 70:
        status = "Normal"
    elif memory.percent < 90:
        status = "Warning"
    else:
        status = "Critical"

    print(f"RAM Status: {status}")


def get_swap_info():
    swap = psutil.swap_memory()

    print("\nSWAP INFORMATION")
    print(f"Total Swap: {swap.total / (1024 ** 3):.2f} GB")
    print(f"Used Swap: {swap.used / (1024 ** 3):.2f} GB")
    print(f"Free Swap: {swap.free / (1024 ** 3):.2f} GB")
    print(f"Swap Usage: {swap.percent}%")


def get_top_memory_processes():
    print("\nTOP 10 RAM PROCESSES")

    processes = []

    for process in psutil.process_iter(
        ['pid', 'name', 'memory_info']
    ):
        try:
            info = process.info
            ram = info['memory_info'].rss / (1024 ** 2)

            processes.append({
                'pid': info['pid'],
                'name': info['name'],
                'ram': ram
            })

        except (psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess):
            continue

    processes.sort(key=lambda p: p['ram'], reverse=True)

    print(f"{'PID':<10}{'PROCESS':<25}{'RAM (MB)':>12}")
    print("-" * 47)

    for process in processes[:10]:
        print(
            f"{process['pid']:<10}"
            f"{process['name'][:24]:<25}"
            f"{process['ram']:>12.2f}"
        )


if __name__ == "__main__":
    get_memory_info()
    get_swap_info()
    get_top_memory_processes()


def get_memory_data():
    import psutil

    memory = psutil.virtual_memory()

    return {
        "total": memory.total / (1024 ** 3),
        "used": memory.used / (1024 ** 3),
        "available": memory.available / (1024 ** 3),
        "percent": memory.percent
    }
