from cpu_logging_v03 import analyze_and_visualize # type: ignore

# ---------------------------
LOG_FILE = "cpu_ram_rdp_log.xlsx"
CHART_FILE = "cpu_ram_rdp_chart.png"
CPU_THRESHOLD = 10
RAM_THRESHOLD = 10
# ---------------------------

def main():
    analyze_and_visualize(LOG_FILE, CHART_FILE, CPU_THRESHOLD, RAM_THRESHOLD)

if __name__ == '__main__':
    main()