import re
with open('app_log_sample.txt') as f:
    logs = f.readlines()

error_logs = [log for log in logs if "ERROR" in log]
pattern = re.compile(r"\[(.*?)\] \[(.*?)\] - (.*)")
structured_logs = [pattern.findall(log)[0] for log in error_logs]

# Connect to SQL and insert logs (pseudo-code shown)
