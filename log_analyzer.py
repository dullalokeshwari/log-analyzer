#log analyzer
#reads a log file and generates a summary report

LOG_FILE ="sample_log.txt"
REPORT_FILE ="report.txt"

info_count = 0
warning_count = 0
error_count = 0
try:
    with open(LOG_FILE, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith("INFO"):
                info_count += 1
            elif line.startswith("WARNING"):
                warning_count += 1
            elif line.startswith("ERROR"):
                error_count += 1

    #DISPLAY RESULT
    print("==== Log Summary Report ====")
    print(f"INFO messages: {info_count}")
    print(f"WARNING messages: {warning_count}")
    print(f"ERROR messages: {error_count}")

    #save report to file
    with open(REPORT_FILE, "w") as report_file:
        report_file.write("==== Log Summary Report ====\n")
        report_file.write(f"INFO messages: {info_count}\n")
        report_file.write(f"WARNING messages: {warning_count}\n")
        report_file.write(f"ERROR messages: {error_count}\n")
        print("\n report generated successfully in report.txt")

except FileNotFoundError:
    print(f"error: {LOG_FILE} not found.")