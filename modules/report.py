
import psutil
import socket
import json
from datetime import datetime
from pathlib import Path


def generate_report():

    print("\nGENERATING SYSTEM REPORT")

    # CPU information
    cpu_info = {
        "usage_percent": psutil.cpu_percent(interval=1),
        "physical_cores": psutil.cpu_count(logical=False),
        "logical_cores": psutil.cpu_count(logical=True)
    }

    # RAM information
    memory = psutil.virtual_memory()

    memory_info = {
        "total_gb": round(memory.total / (1024 ** 3), 2),
        "used_gb": round(memory.used / (1024 ** 3), 2),
        "available_gb": round(memory.available / (1024 ** 3), 2),
        "usage_percent": memory.percent
    }

    # Disk information
    disk = psutil.disk_usage("/")

    disk_info = {
        "total_gb": round(disk.total / (1024 ** 3), 2),
        "used_gb": round(disk.used / (1024 ** 3), 2),
        "free_gb": round(disk.free / (1024 ** 3), 2),
        "usage_percent": disk.percent
    }

    # System information
    system_info = {
        "hostname": socket.gethostname(),
        "boot_time": datetime.fromtimestamp(
            psutil.boot_time()
        ).strftime("%Y-%m-%d %H:%M:%S"),
        "report_time": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    }

    # Complete report
    report = {
        "system": system_info,
        "cpu": cpu_info,
        "memory": memory_info,
        "disk": disk_info
    }

    # Create report directory
    report_dir = Path(__file__).resolve().parent.parent / "reports"
    report_dir.mkdir(exist_ok=True)

    # Save JSON report
    filename = datetime.now().strftime(
        "system_report_%Y%m%d_%H%M%S.json"
    )

    report_path = report_dir / filename

    with report_path.open("w") as file:
        json.dump(report, file, indent=4)

    print("\nReport generated successfully!")
    print(f"File saved at: {report_path}")


if __name__ == "__main__":
    generate_report()
