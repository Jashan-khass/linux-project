# 🖥️ Linux System Manager

A Python-based Linux System Monitoring Application that provides real-time system resource monitoring through both a Command Line Interface (CLI) and a Graphical User Interface (GUI).

Built using Python, Tkinter and psutil, this project helps monitor CPU, RAM, disk, network activity, running processes and overall system health.

## 🚀 Features

### 1. Command Line Interface (CLI)
- Interactive terminal menu
- CPU, RAM and Disk information
- Network information
- System information
- Live system monitoring
- Process monitoring
- Process search using PID or process name
- System health check
- JSON report generation

### 2. Graphical User Interface (GUI)
- Modern dark-themed dashboard
- CPU, RAM and Disk usage cards
- Live resource usage progress bars
- Dynamic resource status indicator
- System information panel
- Running process counter
- Manual dashboard refresh
- Dedicated information windows
- Process monitoring and search
- System health checker
- JSON report generation

### 3. CPU Monitoring
- CPU usage percentage
- Physical and logical CPU cores
- CPU frequency
- CPU usage status

### 4. RAM Monitoring
- Total RAM
- Used RAM
- Available RAM
- RAM usage percentage
- Memory warnings

### 5. Disk Monitoring
- Total disk space
- Used disk space
- Free disk space
- Disk usage percentage
- Disk status

### 6. Network Monitoring
- Network interfaces
- IP addresses
- MAC addresses
- Data sent and received

### 7. Process Monitoring
- Running process list
- Process ID (PID)
- Process name
- Process username
- RAM usage percentage
- Top processes sorted by RAM usage

### 8. System Health Check
- CPU usage monitoring
- RAM usage monitoring
- Disk usage monitoring
- NORMAL, WARNING and CRITICAL status

### 9. JSON Report Generator
- Generate system monitoring reports
- Export system information in JSON format
- Save reports inside the reports directory

## 🛠️ Technologies Used

- Python 3
- psutil – System and process monitoring
- Tkinter – Graphical User Interface
- ttk – GUI widgets and progress bars
- Linux (Ubuntu on WSL2)
- Git and GitHub

## 📁 Project Structure

```text
system-manager/
│
├── app.py
├── main.py
├── gui.py
├── system-info.py
├── README.md
├── .gitignore
│
├── modules/
│   ├── cpu.py
│   ├── memory.py
│   ├── disk.py
│   ├── network.py
│   ├── system.py
│   ├── live.py
│   ├── process.py
│   ├── search.py
│   ├── report.py
│   └── health.py
│
└── reports/
    └── Generated JSON reports
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Jashan-khass/linux-project.git
```

### 2. Navigate to the project directory

```bash
cd linux-project
```

### 3. Install dependencies

On Ubuntu:

```bash
sudo apt update
sudo apt install python3-psutil python3-tk -y
```

## ▶️ How to Run

Start the application launcher:

```bash
python3 app.py
```

Choose your preferred mode:

1. Command Line Interface (CLI)
2. Graphical User Interface (GUI)
3. Exit

You can also run the CLI or GUI separately:

```bash
python3 main.py
```

```bash
python3 gui.py
```

## 🎯 Learning Objectives

- Python programming
- Linux system administration
- System resource monitoring
- Process management and searching
- GUI development using Tkinter
- Modular Python programming
- JSON report generation
- Git and GitHub version control

## 🔮 Future Improvements

- Real-time CPU and RAM usage graphs
- Network speed monitoring
- Advanced process management
- System notifications
- Improved dashboard customization
- Additional report formats

## 👨‍💻 Author

**Jashanpreet Kaur**

GitHub: [@Jashan-khass](https://github.com/Jashan-khass)

Project Repository: [Linux System Manager](https://github.com/Jashan-khass/linux-project)

---

⭐ If you find this project interesting, feel free to explore the repository!
