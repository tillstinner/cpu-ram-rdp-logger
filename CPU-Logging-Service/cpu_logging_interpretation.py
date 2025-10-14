import argparse
import os
from datetime import datetime
from cpu_logging_collect_data_for_service import analyze_and_visualize  # type: ignore

DEFAULT_CPU_THRESHOLD = 10
DEFAULT_RAM_THRESHOLD = 10

def main():
    parser = argparse.ArgumentParser(description="Analyze CPU/RAM log and create chart.")
    parser.add_argument(
        "-input", "--input",
        type=str,
        required=True,
        help="Path to the input log file (with timestamp)"
    )
    parser.add_argument(
        "--cpu",
        type=int,
        default=DEFAULT_CPU_THRESHOLD,
        help=f"CPU usage threshold (default: {DEFAULT_CPU_THRESHOLD})"
    )
    parser.add_argument(
        "--ram",
        type=int,
        default=DEFAULT_RAM_THRESHOLD,
        help=f"RAM usage threshold (default: {DEFAULT_RAM_THRESHOLD})"
    )

    args = parser.parse_args()
    log_file = args.input
    cpu_threshold = args.cpu
    ram_threshold = args.ram

    log_dir = os.path.dirname(log_file)  
    base_name = os.path.basename(log_file)
    name_part, ext = os.path.splitext(base_name)

    if name_part.startswith("cpu_ram_rdp_log_"):
        timestamp = name_part.replace("cpu_ram_rdp_log_", "")
    else:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    chart_file = os.path.join(log_dir, f"cpu_ram_rdp_chart_{timestamp}.png")  

    analyze_and_visualize(log_file, chart_file, cpu_threshold=cpu_threshold, ram_threshold=ram_threshold)

if __name__ == "__main__":
    main()
