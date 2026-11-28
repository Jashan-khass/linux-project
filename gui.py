
import tkinter as tk
from modules.cpu import get_cpu_info
from modules.cpu import get_cpu_data
from modules.memory import get_memory_data
from modules.disk import get_disk_data
from modules.network import get_network_data
from tkinter import ttk
import psutil
from modules.process import get_process_data
from modules.search import find_process_data
from modules.health import get_health_data
from modules.report import generate_report
from tkinter import messagebox
import platform
import datetime
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from collections import deque
# Performance chart data
cpu_history = deque(maxlen=20)
ram_history = deque(maxlen=20)
disk_history = deque(maxlen=20)
time_history = deque(maxlen=20)

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


def show_ram_info():
    ram_window = tk.Toplevel(root)

    ram_window.title("RAM Information")
    ram_window.geometry("400x300")
    ram_window.configure(bg="#1e1e2e")

    ram_data = get_memory_data()

    title = tk.Label(
        ram_window,
        text="RAM INFORMATION",
        font=("Arial", 18, "bold"),
        bg="#1e1e2e",
        fg="white"
    )
    title.pack(pady=20)

    info_text = (
        f"Total RAM: {ram_data['total']:.2f} GB\n"
        f"Used RAM: {ram_data['used']:.2f} GB\n"
        f"Available RAM: {ram_data['available']:.2f} GB\n"
        f"RAM Usage: {ram_data['percent']}%"
    )

    info = tk.Label(
        ram_window,
        text=info_text,
        font=("Arial", 12),
        bg="#1e1e2e",
        fg="white",
        justify="left"
    )
    info.pack(pady=20)


def show_disk_info():
    disk_window = tk.Toplevel(root)

    disk_window.title("Disk Information")
    disk_window.geometry("400x300")
    disk_window.configure(bg="#1e1e2e")

    disk_data = get_disk_data()

    title = tk.Label(
        disk_window,
        text="DISK INFORMATION",
        font=("Arial", 18, "bold"),
        bg="#1e1e2e",
        fg="white"
    )
    title.pack(pady=20)

    info_text = (
        f"Total Storage: {disk_data['total']:.2f} GB\n"
        f"Used Storage: {disk_data['used']:.2f} GB\n"
        f"Free Storage: {disk_data['free']:.2f} GB\n"
        f"Disk Usage: {disk_data['percent']}%"
    )

    info = tk.Label(
        disk_window,
        text=info_text,
        font=("Arial", 12),
        bg="#1e1e2e",
        fg="white",
        justify="left"
    )
    info.pack(pady=20)

def show_network_info():
     network_window = tk.Toplevel(root)
     network_window.title("Network Information")
     network_window.geometry("500x400")
     network_window.configure(bg="#1e1e2e")

     network_data = get_network_data()

     title = tk.Label(
         network_window,
         text="NETWORK INFORMATION",
         font=("Arial", 18, "bold"),
         bg="#1e1e2e",
         fg="white"
     )

     title.pack(pady=20)

     info_text = "NETWORK INTERFACES\n\n"
     for interface in network_data["interfaces"]:
         info_text += (
             f"Interface: {interface['name']}\n"
             f"IP Adress: {interface['ip']}\n\n"
         )

     info_text += (
         f"Data Sent: {network_data['sent']:.2f} MB\n"
         f"Data Received: {network_data['received']:.2f}MB"
     )

     info = tk.Label(
         network_window,
         text=info_text,
         font=("Arial", 11),
         bg="#1e1e2e",
         fg="white",
         justify="left"
     )
     info.pack(pady=20)


def show_process_info():
    process_window = tk.Toplevel(root)

    process_window.title("Process Monitoring")
    process_window.geometry("750x450")
    process_window.configure(bg="#1e1e2e")

    title = tk.Label(
        process_window,
        text="RUNNING PROCESSES",
        font=("Arial", 18, "bold"),
        bg="#1e1e2e",
        fg="white"
    )
    title.pack(pady=15)

    process_text = tk.Text(
        process_window,
        height=20,
        width=85,
        bg="#29293d",
        fg="white",
        font=("Courier", 10)
    )
    process_text.pack(padx=10, pady=10)

    processes = get_process_data()

    process_text.insert(
        tk.END,
        f"{'PID':<10}{'PROCESS NAME':<25}"
        f"{'USERNAME':<20}{'RAM %':<10}\n"
    )

    process_text.insert(tk.END, "-" * 70 + "\n")

    for process in processes:
        process_text.insert(
            tk.END,
            f"{process['pid']:<10}"
            f"{str(process['name']):<25}"
            f"{str(process['username']):<20}"
            f"{process['memory'] or 0:.2f}%\n"
        )

    process_text.config(state="disabled")


def show_search_window():
    search_window = tk.Toplevel(root)

    search_window.title("Process Search")
    search_window.geometry("600x400")
    search_window.configure(bg="#1e1e2e")

    title = tk.Label(
        search_window,
        text="PROCESS SEARCH",
        font=("Arial", 18, "bold"),
        bg="#1e1e2e",
        fg="white"
    )
    title.pack(pady=15)

    search_entry = tk.Entry(
        search_window,
        font=("Arial", 12),
        width=30
    )
    search_entry.pack(pady=10)

    result_box = tk.Text(
        search_window,
        height=12,
        width=65,
        bg="#29293d",
        fg="white",
        font=("Courier", 10)
    )
    result_box.pack(pady=10)

    def search():
        search_term = search_entry.get().strip()

        result_box.config(state="normal")
        result_box.delete("1.0", tk.END)

        if not search_term:
            result_box.insert(tk.END, "Enter PID or process name!")
        else:
            results = find_process_data(search_term)

            if results:
                for process in results:
                    result_box.insert(
                        tk.END,
                        f"PID: {process['pid']}\n"
                        f"Name: {process['name']}\n"
                        f"Username: {process['username']}\n"
                        f"RAM Usage: {process['memory'] or 0:.2f}%\n"
                        f"{'-' * 35}\n"
                    )
            else:
                result_box.insert(tk.END, "Process not found!")

        result_box.config(state="disabled")

    search_button = tk.Button(
        search_window,
        text="Search Process",
        command=search,
        font=("Arial", 11)
    )
    search_button.pack(pady=5)


def show_health_info():
    health_window = tk.Toplevel(root)

    health_window.title("System Health Checker")
    health_window.geometry("500x450")
    health_window.configure(bg="#1e1e2e")

    title = tk.Label(
        health_window,
        text="SYSTEM HEALTH REPORT",
        font=("Arial", 18, "bold"),
        bg="#1e1e2e",
        fg="white"
    )
    title.pack(pady=20)

    data = get_health_data()

    info_text = (
        f"CPU Usage: {data['cpu']}%\n"
        f"RAM Usage: {data['ram']}%\n"
        f"Disk Usage: {data['disk']}%\n\n"
        f"System Status: {data['status']}\n"
    )

    for warning in data["warnings"]:
        info_text += f"\nWARNING: {warning}"

    for message in data["critical"]:
        info_text += f"\nCRITICAL: {message}"

    if data["status"] == "NORMAL":
        info_text += "\n\nAll monitored resources are healthy."

    color = {
        "NORMAL": "#22c55e",
        "WARNING": "#facc15",
        "CRITICAL": "#ef4444"
    }[data["status"]]

    info = tk.Label(
        health_window,
        text=info_text,
        font=("Arial", 12),
        bg="#1e1e2e",
        fg=color,
        justify="left"
    )
    info.pack(pady=20)


def generate_gui_report():
    try:
        generate_report()

        messagebox.showinfo(
            "Report Generated",
            "System report generated successfully!\n\n"
            "Please check the reports folder."
        )

    except Exception as error:
        messagebox.showerror(
            "Report Error",
            f"Unable to generate report:\n{error}"
        )



def refresh_dashboard_now():
    cpu = psutil.cpu_percent(interval=None)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    cpu_bar["value"] = cpu
    ram_bar["value"] = ram
    disk_bar["value"] = disk

    cpu_label.config(text=f"CPU Usage: {cpu:.1f}%")
    ram_label.config(text=f"RAM Usage: {ram:.1f}%")
    disk_label.config(text=f"DISK Usage: {disk:.1f}%")
    # Store latest performance readings
    cpu_history.append(cpu)
    ram_history.append(ram)
    disk_history.append(disk)

    # Update chart data
    x_values = list(range(len(cpu_history)))

    cpu_line.set_data(x_values, list(cpu_history))
    ram_line.set_data(x_values, list(ram_history))
    disk_line.set_data(x_values, list(disk_history))

    # Update all three charts
    for chart in axes:
        chart.set_xlim(0, 19)
        chart.set_xticks(x_values)
        chart.set_xticklabels(
            list(time_history),
            rotation=45,
            fontsize=6,
            color="white"
        )

    # Refresh charts
    chart_canvas.draw_idle()

    highest_usage = max(cpu, ram, disk)

    if highest_usage >= 90:
        status = "CRITICAL"
        color = "#f38ba8"
    elif highest_usage >= 80:
        status = "WARNING"
        color = "#f9e2af"
    else:
        status = "NORMAL"
        color = "#a6e3a1"

    status_label.config(
        text=f"SYSTEM STATUS: {status}",
        fg=color
    )


def refresh_process_count_now():
    count = len(psutil.pids())

    process_count_label.config(
        text=f"Running Processes: {count}"
    )


def refresh_all():
    refresh_dashboard_now()
    refresh_process_count_now()

    last_updated_label.config(
        text="Last Updated: " +
        datetime.datetime.now().strftime("%H:%M:%S")
    )


def update_dashboard():
    refresh_dashboard_now()
    root.after(1000, update_dashboard)


def update_process_count():
    refresh_process_count_now()
    root.after(2000, update_process_count)



     
# Main application window
root = tk.Tk()

# Window title
root.title("Linux System Manager")

# Window size
root.geometry("900x780")

# Window background
root.configure(bg="#1e1e2e")


# Professional dark theme

root.minsize(800, 700)
# SCROLLABLE DASHBOARD

main_container = tk.Frame(root, bg="#1e1e2e")
main_container.pack(fill="both", expand=True)

canvas = tk.Canvas(
    main_container,
    bg="#1e1e2e",
    highlightthickness=0
)

scrollbar = ttk.Scrollbar(
    main_container,
    orient="vertical",
    command=canvas.yview
)

canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

content_frame = tk.Frame(canvas, bg="#1e1e2e")

canvas_window = canvas.create_window(
    (0, 0),
    window=content_frame,
    anchor="nw"
)

def update_scroll_region(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

# Mouse wheel scrolling (Linux)
def on_mousewheel(event):
    if event.num == 4:
        canvas.yview_scroll(-1, "units")
    elif event.num == 5:
        canvas.yview_scroll(1, "units")

canvas.bind_all("<Button-4>", on_mousewheel)
canvas.bind_all("<Button-5>", on_mousewheel)

content_frame.bind("<Configure>", update_scroll_region)

canvas.bind(
    "<Configure>",
    lambda event: canvas.itemconfigure(
        canvas_window,
        width=event.width
    )
)

# Default button styling
root.option_add("*Button.background", "#313244")
root.option_add("*Button.foreground", "white")
root.option_add("*Button.activeBackground", "#45475a")
root.option_add("*Button.activeForeground", "white")
root.option_add("*Button.font", ("Arial", 11, "bold"))
root.option_add("*Button.relief", "flat")
root.option_add("*Button.borderWidth", 0)
root.option_add("*Button.cursor", "hand2")

# Entry styling
root.option_add("*Entry.background", "#313244")
root.option_add("*Entry.foreground", "white")
root.option_add("*Entry.insertBackground", "white")

# Progress bar styling
style = ttk.Style(root)
style.theme_use("clam")

# CPU Progress Bar
style.configure(
    "CPU.Horizontal.TProgressbar",
    thickness=12,
    troughcolor="#45475a",
    background="#89b4fa"
)

# RAM Progress Bar
style.configure(
    "RAM.Horizontal.TProgressbar",
    thickness=12,
    troughcolor="#45475a",
    background="#a6e3a1"
)

# DISK Progress Bar
style.configure(
    "DISK.Horizontal.TProgressbar",
    thickness=12,
    troughcolor="#45475a",
    background="#f9e2af"
)


# MAIN DASHBOARD HEADER

header_frame = tk.Frame(content_frame, bg="#1e1e2e")
header_frame.pack(fill="x", padx=30, pady=(25, 10))

heading = tk.Label(
    header_frame,
    text="LINUX SYSTEM MANAGER",
    font=("Arial", 24, "bold"),
    bg="#1e1e2e",
    fg="#89b4fa"
)
heading.pack(anchor="w")

message = tk.Label(
    header_frame,
    text="Real-Time System Monitoring Dashboard",
    font=("Arial", 11),
    bg="#1e1e2e",
    fg="#a6adc8"
)
message.pack(anchor="w", pady=5)

# Manual Refresh Button

refresh_button = tk.Button(
    header_frame,
    text="⟳  REFRESH DASHBOARD",
    command=refresh_all,
    font=("Arial", 10, "bold"),
    padx=15,
    pady=8,
    cursor="hand2"
)

refresh_button.pack(anchor="e", pady=8)

last_updated_label = tk.Label(
    header_frame,
    text="Last Updated: Waiting...",
    font=("Arial", 9),
    bg="#1e1e2e",
    fg="#a6adc8"
)

last_updated_label.pack(anchor="e")


# RESOURCE MONITORING CARDS

dashboard_frame = tk.Frame(content_frame, bg="#1e1e2e")
dashboard_frame.pack(fill="x", padx=25, pady=15)

dashboard_frame.columnconfigure((0, 1, 2), weight=1)

def create_metric_card(parent, title, column):
    card = tk.Frame(
        parent,
        bg="#313244",
        padx=15,
        pady=15
    )
    card.grid(
        row=0,
        column=column,
        padx=8,
        sticky="nsew"
    )

    label = tk.Label(
        card,
        text=f"{title} Usage: 0%",
        font=("Arial", 12, "bold"),
        bg="#313244",
        fg="white"
    )
    label.pack(pady=8)

    bar = ttk.Progressbar(
        card,
        length=180,
        maximum=100,
        style=f"{title}.Horizontal.TProgressbar"
    )
    bar.pack(pady=8, fill="x")

    return label, bar


cpu_label, cpu_bar = create_metric_card(
    dashboard_frame, "CPU", 0
)

ram_label, ram_bar = create_metric_card(
    dashboard_frame, "RAM", 1
)

disk_label, disk_bar = create_metric_card(
    dashboard_frame, "DISK", 2
)

# LIVE PERFORMANCE CHART

chart_frame = tk.Frame(content_frame, bg="#313244")
chart_frame.pack(fill="x", padx=35, pady=10)

figure = Figure(figsize=(8, 2.8), dpi=100)
figure.patch.set_facecolor("#313244")

axes = figure.subplots(1, 3)

cpu_line, = axes[0].plot([], [], color="#89b4fa")
ram_line, = axes[1].plot([], [], color="#a6e3a1")
disk_line, = axes[2].plot([], [], color="#f9e2af")

titles = ["CPU Usage", "RAM Usage", "Disk Usage"]

for chart, title in zip(axes, titles):
    chart.set_title(title, color="white", fontsize=10)
    chart.set_ylim(0, 100)
    chart.set_xlim(0, 19)
    chart.set_facecolor("#1e1e2e")
    chart.tick_params(colors="white", labelsize=7)
    chart.grid(color="#45475a", linestyle="--", alpha=0.5)

figure.tight_layout()

chart_canvas = FigureCanvasTkAgg(
    figure,
    master=chart_frame
)

chart_canvas.get_tk_widget().pack(fill="x")

# SYSTEM STATUS INDICATOR

status_frame = tk.Frame(content_frame, bg="#1e1e2e")
status_frame.pack(fill="x", padx=35, pady=10)

status_label = tk.Label(
    status_frame,
    text="SYSTEM STATUS: NORMAL",
    font=("Arial", 12, "bold"),
    bg="#1e1e2e",
    fg="#a6e3a1"
)

status_label.pack(anchor="w")

# SYSTEM INFORMATION PANEL

system_frame = tk.Frame(
    content_frame,
    bg="#313244",
    padx=15,
    pady=12
)

system_frame.pack(fill="x", padx=35, pady=10)

system_title = tk.Label(
    system_frame,
    text="SYSTEM INFORMATION",
    font=("Arial", 13, "bold"),
    bg="#313244",
    fg="#cba6f7"
)

system_title.pack(anchor="w", pady=5)

hostname = platform.node()
os_name = platform.system()
processor = platform.processor() or "Not Available"

system_info = tk.Label(
    system_frame,
    text=(
        f"Hostname: {hostname}\n"
        f"Operating System: {os_name}\n"
        f"Processor: {processor}"
    ),
    font=("Arial", 10),
    bg="#313244",
    fg="white",
    justify="left"
)

system_info.pack(anchor="w", pady=5)

process_frame = tk.Frame(
    content_frame,
    bg="#313244",
    padx=15,
    pady=12
)

process_frame.pack(fill="x", padx=35, pady=10)

process_title = tk.Label(
    process_frame,
    text="PROCESS MONITOR",
    font=("Arial", 13, "bold"),
    bg="#313244",
    fg="#89b4fa"
)

process_title.pack(anchor="w")

process_count_label = tk.Label(
    process_frame,
    text="Running Processes:0",
    font=("Arial", 12, "bold"),
    bg="#313244",
    fg="white"
)

process_count_label.pack(anchor="w", pady=8)

# SYSTEM TOOLS SECTION

tools_title = tk.Label(
    content_frame,
    text="SYSTEM TOOLS",
    font=("Arial", 16, "bold"),
    bg="#1e1e2e",
    fg="#cba6f7"
)
tools_title.pack(anchor="w", padx=35, pady=(15, 10))

tools_frame = tk.Frame(content_frame, bg="#1e1e2e")
tools_frame.pack(fill="x", padx=30)

tools_frame.columnconfigure((0, 1), weight=1)

def create_tool_button(parent, text, command, row, column):
    button = tk.Button(
        parent,
        text=text,
        command=command,
        font=("Arial", 11, "bold"),
        width=25,
        pady=12,
        cursor="hand2"
    )
    button.grid(
        row=row,
        column=column,
        padx=10,
        pady=8,
        sticky="ew"
    )


create_tool_button(
    tools_frame, "CPU Information",
    show_cpu_info, 0, 0
)

create_tool_button(
    tools_frame, "RAM Information",
    show_ram_info, 0, 1
)

create_tool_button(
    tools_frame, "Disk Information",
    show_disk_info, 1, 0
)

create_tool_button(
    tools_frame, "Network Information",
    show_network_info, 1, 1
)

create_tool_button(
    tools_frame, "Process Monitoring",
    show_process_info, 2, 0
)

create_tool_button(
    tools_frame, "Process Search",
    show_search_window, 2, 1
)

create_tool_button(
    tools_frame, "System Health Check",
    show_health_info, 3, 0
)

create_tool_button(
    tools_frame, "Generate JSON Report",
    generate_gui_report, 3, 1
)

# Start live dashboard
update_dashboard()

# ===== DASHBOARD FOOTER =====

footer = tk.Label(
    root,
    text="Linux System Manager | Built with Python & Tkinter",
    font=("Arial", 9),
    bg="#1e1e2e",
    fg="#6c7086"
)

footer.pack(side="bottom", pady=15)

update_process_count()

# Start GUI application
root.mainloop()
