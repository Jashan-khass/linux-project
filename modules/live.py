
import psutil
import time
import os


def live_monitor():

    try:
        while True:

            os.system("clear")

            print("     LIVE SYSTEM MONITOR")

            # CPU Monitoring
            cpu = psutil.cpu_percent(interval=1)

            # RAM Monitoring
            ram = psutil.virtual_memory()

            # Disk Monitoring
            disk = psutil.disk_usage("/")

            print(f"\nCPU Usage: {cpu}%")
            print(f"RAM Usage: {ram.percent}%")
            print(f"Disk Usage: {disk.percent}%")

            print("\nPress CTRL + C to stop monitoring")

    except KeyboardInterrupt:
        print("\nLive Monitoring Stopped!")


if __name__ == "__main__":
    live_monitor()
