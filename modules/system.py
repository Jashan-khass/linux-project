
import psutil
import socket
from datetime import datetime, timedelta


def get_system_info():

    print("\nSYSTEM INFORMATION")

    # Hostname
    hostname = socket.gethostname()

    # System boot time
    boot_timestamp = psutil.boot_time()
    boot_time = datetime.fromtimestamp(boot_timestamp)

    # Current time
    current_time = datetime.now()

    # Calculate uptime
    uptime = current_time - boot_time

    # Convert uptime into readable format
    uptime = str(timedelta(seconds=int(uptime.total_seconds())))

    print(f"Hostname: {hostname}")
    print(f"Boot Time: {boot_time}")
    print(f"System Uptime: {uptime}")


if __name__ == "__main__":
    get_system_info()
