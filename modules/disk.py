import psutil


def get_disk_info():

    print("\nDISK INFORMATION")

    disk = psutil.disk_usage("/")

    total = disk.total / (1024 ** 3)
    used = disk.used / (1024 ** 3)
    free = disk.free / (1024 ** 3)
    percentage = disk.percent

    print(f"Total Disk: {total:.2f} GB")
    print(f"Used Disk: {used:.2f} GB")
    print(f"Free Disk: {free:.2f} GB")
    print(f"Disk Usage: {percentage}%")

    if percentage > 90:
        print("WARNING: Disk Space Almost Full!")
    elif percentage > 75:
        print("Disk Status: Moderate")
    else:
        print("Disk Status: Normal")


if __name__ == "__main__":
    get_disk_info()
