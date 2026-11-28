
import psutil
import time


def get_cpu_info():

    print("\nCPU INFORMATION")

    # CPU usage percentage
    cpu_usage = psutil.cpu_percent(interval=1)

    # CPU core information
    physical_cores = psutil.cpu_count(logical=False)
    logical_cores = psutil.cpu_count(logical=True)

    # CPU frequency
    frequency = psutil.cpu_freq()

    print(f"CPU Usage: {cpu_usage}%")
    print(f"Physical Cores: {physical_cores}")
    print(f"Logical Cores: {logical_cores}")

    if frequency:
        print(f"CPU Frequency: {frequency.current:.2f} MHz")
    if cpu_usage > 80:
        print("High CPU usage!")
    else:
        print("CPU Status: Normal")



if __name__ == "__main__":
    get_cpu_info()

def get_cpu_data():
    import psutil

    cpu_usage = psutil.cpu_percent(interval=None)
    physical_cores = psutil.cpu_count(logical=False)
    logical_cores = psutil.cpu_count(logical=True)
    frequency = psutil.cpu_freq()

    return{
        "usage": cpu_usage,
        "physical_cores": physical_cores,
        "logical_cores": logical_cores,
        "frequency": frequency.current if frequency else 0
    }
