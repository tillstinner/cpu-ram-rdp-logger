# CPU Logging Dashboard Module

Web-based dashboard for **real-time monitoring of multiple clients**, visualizing metrics collected by the CPU Logging Service.

![CPU/RAM/RDP Dashboard](dashboard_img.png)

## Features

* Displays CPU %, RAM %, and RDP activity for multiple hosts.
* Live updates every 5 seconds.
* Input thresholds for CPU and RAM to calculate % of time above thresholds.
* Summary bars display percentage and actual time (seconds) above thresholds.
* Handles gaps in logging and breaks RDP lines when state changes.
* Fully responsive chart with full-width display and fixed 1050px height.

## Installation

### Dependencies:
```bash
pip install -r requirements.txt
```

### Running

Start the Django server (default port 8000):
```bash
python manage.py runserver
```

Access the dashboard at:
```
http://<server-ip>:8000/dashboard/
```

### Client Service

The client service collects and sends metrics to the dashboard. Run the following script on each client machine:
```
CPU-Logging-Dashboard\Logging-Service\cpu_logging_service_dashboard.py
```

* Make sure to set `API_URL` in the script to point to the Django server's IP address.
* Run it the same way as the original service module.

## Usage

1. Select the host and time range.
2. Adjust CPU/RAM thresholds to see time-over-threshold calculations update live.
3. Visual summary shows bars and seconds spent above thresholds.

---

**Note:**

* Ensure the client service is running on each host you want to monitor.
* The dashboard will only display data from hosts actively sending metrics to the server.

