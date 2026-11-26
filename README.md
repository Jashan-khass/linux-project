# 🖥️ Linux System Manager

A Python-based Linux system monitoring application that provides essential system information and resource usage statistics through an interactive terminal menu.

This project is being developed to build practical skills in **Python Programming, Linux System Administration, Git, and System Monitoring**.

## 🚀 Features

### 1. System Information
- Username
- Operating System
- Kernel Version
- Machine Architecture
- Current Working Directory
- Date and Time

### 2. CPU Monitoring
- CPU Usage Percentage
- Physical CPU Cores
- Logical CPU Cores
- CPU Frequency
- CPU Usage Status (Normal, Moderate, High)

### 3. RAM Monitoring
- Total RAM
- Used RAM
- Available RAM
- RAM Usage Percentage
- High RAM Usage Warning

### 4. Disk Monitoring
- Total Disk Space
- Used Disk Space
- Free Disk Space
- Disk Usage Percentage
- Disk Status

### 5. Network Monitoring
- Network Interfaces
- IP Address
- MAC Address
- Data Sent
- Data Received

### 6. System Monitoring
- Hostname
- System Boot Time
- System Uptime

### 7. Live System Monitoring
- Continuous CPU Usage Monitoring
- Continuous RAM Usage Monitoring
- Continuous Disk Usage Monitoring
- Stop monitoring using `Ctrl + C`

### 8. Process Monitoring
- Running Process List
- Process ID (PID)
- Process Name
- Process Username
- RAM Usage Percentage
- Top 15 processes sorted by RAM usage

## 🛠️ Technologies Used

- **Python 3**
- **psutil** – System and process monitoring
- **Linux (Ubuntu on WSL2)**
- **Git & GitHub**

## 📁 Project Structure

```text
linux-project/
│
├── README.md
├── .gitignore
├── main.py
├── system-info.py
│
└── modules/
    ├── cpu.py
    ├── memory.py
    ├── disk.py
    ├── network.py
    ├── system.py
    ├── live.py
    └── process.py
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
sudo apt install python3-psutil -y
```

Alternatively:

```bash
python3 -m pip install psutil
```

## ▶️ Usage

Start the interactive system manager:

```bash
python3 main.py
```

You can also run individual modules:

```bash
python3 system-info.py
python3 modules/cpu.py
python3 modules/memory.py
python3 modules/disk.py
python3 modules/network.py
python3 modules/system.py
python3 modules/live.py
python3 modules/process.py
```

Stop live monitoring with `Ctrl + C`.

## 🎯 Learning Objectives

- Learn Python through practical projects.
- Understand Linux system administration.
- Monitor CPU, RAM, disk, and network resources.
- Understand Linux processes and resource usage.
- Practice Python functions, loops, conditions, and exception handling.
- Learn modular Python project organization.
- Build confidence with Git and GitHub.

## 🔮 Future Improvements

- Real-time CPU and RAM graphs
- Process CPU usage monitoring
- Process search and filtering
- JSON and TXT report generation
- System alerts and logging
- Interactive process management
- Improved error handling
- Better terminal interface

## 👨‍💻 Author

**Jashanpreet Kaur**

GitHub: [@Jashan-khass](https://github.com/Jashan-khass)

Project Repository: [Linux System Manager](https://github.com/Jashan-khass/linux-project)

---

⭐ If you find this project interesting, feel free to explore the repository!
