# CPU Logging Repository

This repository contains two main modules for monitoring CPU, RAM, and RDP usage on Windows systems:

1. **CPU-Logging-Service** – runs as a Windows service for background monitoring.
2. **CPU-Logging** – standalone terminal-based version for manual execution and interactive logging.


# Module 1: CPU-Logging-Service

A Windows service for continuously monitoring CPU and RAM usage, as well as active RDP sessions, logging the data to Excel files.

![CPU/RAM/RDP Chart](CPU-Logging-Service/example_chart.png)

## Features

* Continuous background monitoring as a Windows service.
* Logs CPU, RAM, and RDP activity to timestamped Excel files.
* Manual analysis and visualization via `cpu_logging_interpretation.py`.
* Graceful stop supported.

## Installation

### Dependencies:

```bash
pip install -r requirements.txt  # specific to CPU-Logging-Service
```

### Windows Service Installation

```cmd
python cpu_logging_service.py install
python cpu_logging_service.py start
python cpu_logging_service.py stop
python cpu_logging_service.py remove
```

> Logs are saved by default to `C:\CPU-Logging-Service\Logs`, interval: 2 seconds.

## Manual Analysis

```bash
python cpu_logging_interpretation.py --input "C:\Logs\cpu_ram_rdp_log_YYYY-MM-DD_HH-MM-SS.xlsx" --cpu 80 --ram 70
```

# Module 2: CPU-Logging (Predecessor)

Terminal-based logging and analysis tool. Data is collected in Excel and simultaneously printed to the console.

## Features

* Interactive terminal mode.
* Logs CPU, RAM, and RDP activity to Excel with timestamped filenames.
* Displays real-time values in the console.
* Automatically generates summary statistics and charts after logging.

## Usage

Run the main script:

```bash
python cpu_logging_v04.py
```

* Enter the duration in seconds (0 for infinite) when prompted.
* Logs are saved as `cpu_ram_rdp_log_<timestamp>.xlsx`.
* After logging, analyze and visualize using:

```bash
python cpu_logging_auswertung_v02.py --input "cpu_ram_rdp_log_<timestamp>.xlsx" --cpu 80 --ram 70
```

* Charts are saved as `cpu_ram_rdp_chart_<timestamp>.png` and embedded in the Excel summary.

## Dependencies

```bash
pip install -r requirements_logging.txt  # specific to CPU-Logging module
```

---

# Author

Till Stinner

# License

MIT License

---

**Note:**

* CPU-Logging-Service is intended for continuous background monitoring.
* CPU-Logging is intended for interactive, terminal-based logging and is the predecessor of the service version.
