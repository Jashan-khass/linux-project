
from modules.cpu import get_cpu_info
from modules.memory import get_memory_info
from modules.disk import get_disk_info
from modules.network import get_network_info
from modules.system import get_system_info

def main_menu():

    while True:

        print("     LINUX SYSTEM MANAGER")

        print("1. CPU Information")
        print("2. RAM Information")
        print("3. Disk Information")
        print("4. Network Information")
        print("5. System Information")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            get_cpu_info()

        elif choice == "2":
            get_memory_info()

        elif choice == "3":
            get_disk_info()

        elif choice == "4":
            get_network_info()
         
        elif choice == "5":
            get_system_info()

        elif choice == "6":
            print("Exiting Linux System Manager...")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main_menu()
