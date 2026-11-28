
import psutil


def get_system_health():

    print("\nSYSTEM HEALTH CHECK")

    # CPU Check
    cpu_usage = psutil.cpu_percent(interval=1)

    # RAM Check
    ram_usage = psutil.virtual_memory().percent

    # Disk Check
    disk_usage = psutil.disk_usage("/").percent

    print(f"\nCPU Usage: {cpu_usage}%")
    print(f"RAM Usage: {ram_usage}%")
    print(f"Disk Usage: {disk_usage}%")

    warnings = []
    critical = []

    # CPU Health
    if cpu_usage >= 90:
        critical.append("CPU usage is critically high!")
    elif cpu_usage >= 80:
        warnings.append("CPU usage is high!")

    # RAM Health
    if ram_usage >= 90:
        critical.append("RAM usage is critically high!")
    elif ram_usage >= 80:
        warnings.append("RAM usage is high!")

    # Disk Health
    if disk_usage >= 95:
        critical.append("Disk space is critically low!")
    elif disk_usage >= 90:
        warnings.append("Disk space is running low!")

    # Display Results
    print("\nHEALTH STATUS")

    if critical:
        print("CRITICAL STATUS")

        for message in critical:
            print("CRITICAL:", message)

    elif warnings:
        print("WARNING STATUS")

        for message in warnings:
            print("WARNING:", message)

    else:
        print("SYSTEM HEALTH: NORMAL")
        print("All monitored resources are within limits.")


if __name__ == "__main__":
    get_system_health()


def get_health_data():
    import psutil

    cpu = psutil.cpu_percent(interval=None)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    warnings = []
    critical = []

    if cpu >= 90:
        critical.append("CPU usage is critically high!")
    elif cpu >= 80:
        warnings.append("CPU usage is high!")

    if ram >= 90:
        critical.append("RAM usage is critically high!")
    elif ram >= 80:
        warnings.append("RAM usage is high!")

    if disk >= 95:
        critical.append("Disk space is critically low!")
    elif disk >= 90:
        warnings.append("Disk space is running low!")

    if critical:
        status = "CRITICAL"
    elif warnings:
        status = "WARNING"
    else:
        status = "NORMAL"

    return {
        "cpu": cpu,
        "ram": ram,
        "disk": disk,
        "status": status,
        "warnings": warnings,
        "critical": critical
    }
