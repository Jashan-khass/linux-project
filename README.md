# 🖥️ Linux System Manager

A Python-based Linux System Monitoring Tool that collects and displays important system information using the `psutil` library.

This project is being developed step by step to improve my Python programming and Linux administration skills.

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

## 🛠️ Technologies Used

- Python 3
- Linux (Ubuntu on WSL2)
- Git & GitHub
- psutil

## 📁 Project Structure

```text
system-manager/
│
├── README.md
├── system-info.py
│
└── modules/
    ├── cpu.py
    ├── memory.py
    ├── disk.py
    └── network.py
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Jashan-khass/linux-project.git
```

### 2. Open the project directory

```bash
cd linux-project
```

### 3. Install dependency

```bash
sudo apt update
sudo apt install python3-psutil -y
```

## ▶️ Usage

Run the main system information script:

```bash
python3 system-info.py
```

Run individual monitoring modules:

```bash
python3 modules/cpu.py
python3 modules/memory.py
python3 modules/disk.py
python3 modules/network.py
```

## 🎯 Project Goals

- Learn Python programming through practical projects.
- Understand Linux system administration.
- Monitor CPU, RAM, disk, and network resources.
- Build a modular system monitoring application.
- Improve Git and GitHub workflow skills.

## 🔮 Future Improvements

- Interactive terminal menu
- Real-time system monitoring
- Process monitoring
- JSON and TXT report generation
- System alerts and logging
- Improved error handling

## 👨‍💻 Author

**Jashanpreet Kaur**

GitHub: [@Jashan-khass](https://github.com/Jashan-khass)

---

⭐ If you find this project interesting, feel free to explore the repository!
