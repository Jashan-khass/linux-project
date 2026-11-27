
import psutil
import socket
import json
from datetime import datetime
from pathlib import Path


def generate_report():

    print("\nGENERATING ADVANCED SYSTEM REPORT")

    # CPU Information
    cpu_info = {
        "usage_percent": psutil.cpu_percent(interval=1),
        "physical_cores": psutil.cpu_count(logical=False),
        "logical_cores": psutil.cpu_count(logical=True)
    }

    # RAM Information
    memory = psutil.virtual_memory()

    memory_info = {
        "total_gb": round(memory.total / (1024 ** 3), 2),
        "used_gb": round(memory.used / (1024 ** 3), 2),
        "available_gb": round(memory.available / (1024 ** 3), 2),
        "usage_percent": memory.percent
    }

    # Disk Information
    disk = psutil.disk_usage("/")

    disk_info = {
        "total_gb": round(disk.total / (1024 ** 3), 2),
        "used_gb": round(disk.used / (1024 ** 3), 2),
        "free_gb": round(disk.free / (1024 ** 3), 2),
        "usage_percent": disk.percent
    }

    # System Information
    system_info = {
        "hostname": socket.gethostname(),
        "boot_time": datetime.fromtimestamp(
            psutil.boot_time()
        ).strftime("%Y-%m-%d %H:%M:%S"),
        "report_time": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    }

    # Network Information
    network_info = {}

    interfaces = psutil.net_if_addrs()
    network_stats = psutil.net_io_counters(pernic=True)

    for interface, addresses in interfaces.items():

        interface_info = {
            "ip_addresses": [],
            "mac_address": None,
            "bytes_sent": 0,
            "bytes_received": 0
        }

        for address in addresses:

            if address.family == socket.AF_INET:
                interface_info["ip_addresses"].append(
                    address.address
                )

            elif address.family == socket.AF_INET6:
                interface_info["ip_addresses"].append(
                    address.address
                )

            elif address.family == psutil.AF_LINK:
                interface_info["mac_address"] = address.address

        if interface in network_stats:
            interface_info["bytes_sent"] = (
                network_stats[interface].bytes_sent
            )

            interface_info["bytes_received"] = (
                network_stats[interface].bytes_recv
            )

        network_info[interface] = interface_info

    # Top 10 RAM-consuming Processes
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
                "memory_percent": round(
                    info["memory_percent"] or 0, 2
                )
            })

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    processes.sort(
        key=lambda item: item["memory_percent"],
        reverse=True
    )

    top_processes = processes[:10]

    # Complete Report
    report = {
        "system": system_info,
        "cpu": cpu_info,
        "memory": memory_info,
        "disk": disk_info,
        "network": network_info,
        "top_10_processes": top_processes
    }

    # Save JSON Report
    report_dir = (
        Path(__file__).resolve().parent.parent / "reports"
    )

    report_dir.mkdir(exist_ok=True)

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
