import psutil
import socket


def get_network_info():

    print("\nNETWORK INFORMATION")

    interfaces = psutil.net_if_addrs()
    stats = psutil.net_io_counters(pernic=True)

    for interface, addresses in interfaces.items():

        print(f"\nInterface: {interface}")

        for address in addresses:

            if address.family == socket.AF_INET:
                print(f"IP Address: {address.address}")

            elif address.family == psutil.AF_LINK:
                print(f"MAC Address: {address.address}")

        if interface in stats:
            sent = stats[interface].bytes_sent / (1024 ** 2)
            received = stats[interface].bytes_recv / (1024 ** 2)

            print(f"Data Sent: {sent:.2f} MB")
            print(f"Data Received: {received:.2f} MB")


if __name__ == "__main__":
    get_network_info()


def get_network_data():
    import psutil
    import socket

    interfaces = psutil.net_if_addrs()
    network_stats = psutil.net_io_counters()

    interface_data = []

    for interface, addresses in interfaces.items():
        for address in addresses:
            if address.family == socket.AF_INET:
                interface_data.append({
                    "name": interface,
                    "ip": address.address
                })

    return {
        "interfaces": interface_data,
        "sent": network_stats.bytes_sent / (1024 ** 2),
        "received": network_stats.bytes_recv / (1024 ** 2)
    }
