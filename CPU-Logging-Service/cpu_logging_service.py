import win32serviceutil
import win32service
import win32event
import servicemanager
import socket
import time
import os
from datetime import datetime
from cpu_logging_collect_data_for_service import collect_data_xlsx  

# -------- Parameters --------
INTERVAL = 2
LOG_DIR = r"C:\CPU-Logging-Service\Logs"
# ----------------------------

class CPUMonitorService(win32serviceutil.ServiceFramework):
    _svc_name_ = "CPURAMLogger"
    _svc_display_name_ = "CPU & RAM Logger Service"
    _svc_description_ = "Monitors CPU, RAM, and RDP usage in the background and logs to Excel."

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.stop_event = win32event.CreateEvent(None, 0, 0, None)
        self.running = True

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        self.running = False
        win32event.SetEvent(self.stop_event)

    def SvcDoRun(self):
        servicemanager.LogInfoMsg("CPU/RAM Logger Service started.")
        self.ReportServiceStatus(win32service.SERVICE_RUNNING)
        self.main()

    def main(self):

        
        os.makedirs(LOG_DIR, exist_ok=True)
        LOG_FILE = os.path.join(LOG_DIR, f"cpu_ram_rdp_log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.xlsx")

        while self.running:
            try:
                collect_data_xlsx(filename=LOG_FILE, should_comtinue=lambda: self.running, interval=INTERVAL, laufzeit=0)
            except Exception as e:
                servicemanager.LogErrorMsg(f"Error in service: {str(e)}")
                time.sleep(5)


if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(CPUMonitorService)
