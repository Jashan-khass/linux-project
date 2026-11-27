
import subprocess
import sys

def main():

    print("\nLINUX SYSTEM MANAGER")
    print("1. Command Line Interface (CLI)")
    print("2. Graphical User Interface (GUI)")
    print("3. Exit")

    choice = input("\nChoose Application Mode: ")

    if choice == "1":
        print("\nStarting CLI...")
        subprocess.run([sys.executable, "main.py"])

    elif choice == "2":
        print("\nStarting GUI...")
        subprocess.run([sys.executable, "gui.py"])

    elif choice == "3":
        print("Exiting Application...")

    else:
        print("Invalid Choice!")

if __name__ == "__main__":
    main()
