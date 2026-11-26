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
