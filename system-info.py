import os 
import platform
import getpass
import datetime
import shutil

print("=" * 40)
print("        LINUX SYSTEM MANAGER")
print("=" * 40)

print("Username:", getpass.getuser())
print("Operating System:", platform.system())
print("Linux Version:", platform.release())
print("Machine:", platform.machine())
print("Current Directory:", os.getcwd())
print("Date & Time:", datetime.datetime.now())

total, used, free = shutil.disk_usage("/")

print("\nDisk Information")
print("Total:", round(total/ (1024**3), 2), "GB")
print("Used:", round(used/ (1024**3), 2), "GB")
print("Free:", round(free/ (1024**3), 2), "GB")

print("\nSystem Manager Completed!")

