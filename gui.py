
import tkinter as tk
from modules.cpu import get_cpu_info
from modules.cpu import get_cpu_data

def show_cpu_info():
    cpu_window = tk.Toplevel(root)
    cpu_window.title("CPU Information")
    cpu_window.geometry("400x300")
    cpu_window.configure(bg="#1e1e2e")

    cpu_data = get_cpu_data()

    title = tk.Label(
        cpu_window,
        text="CPU Information",
        font=("Arial", 18, "bold"),
        bg="#1e1e2e",
        fg="white"
    )
    title.pack(pady=20)

    info_text = (
        f"CPU Usage: {cpu_data['usage']}%\n"
        f"Phyiscal Cores: {cpu_data['physical_cores']}\n"
        f"Logical Cores: {cpu_data['logical_cores']}\n"
        f"frequency; {cpu_data['frequency']:.2f} MHz"
    )

    info = tk.Label(
        cpu_window,
        text=info_text,
        font=("Arial", 12),
        bg="#1e1e2e",
        fg="white",
        justify="left"
    )
    info.pack(pady=20)
     
# Main application window
root = tk.Tk()

# Window title
root.title("Linux System Manager")

# Window size
root.geometry("600x400")

# Window background
root.configure(bg="#1e1e2e")

# Heading
heading = tk.Label(
    root,
    text="LINUX SYSTEM MANAGER",
    font=("Arial", 20, "bold"),
    bg="#1e1e2e",
    fg="white"
)

heading.pack(pady=30)

# Welcome message
message = tk.Label(
    root,
    text="Welcome to your System Manager!",
    font=("Arial", 12),
    bg="#1e1e2e",
    fg="white"
)

message.pack(pady=10)

# CPU button
cpu_button = tk.Button(
    root,
    text="CPU Information",
    font=("Arial", 12),
    width=25,
    command=show_cpu_info
)

cpu_button.pack(pady=10)

# RAM Button
ram_button = tk.Button(
    root,
    text="RAM Information",
    font=("Arial", 12),
    width=25,
    command=lambda: print("RAM BUtton Clicked!")
)

ram_button.pack(pady=10)

# Start GUI application
root.mainloop()
