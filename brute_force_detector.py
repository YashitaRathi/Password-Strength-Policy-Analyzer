from collections import defaultdict

log_file = "sample_login_log.txt"
threshold = 3

failed_attempts = defaultdict(int)

with open(log_file, "r") as file:
    for line in file:
        if "Failed login" in line:
            parts = line.strip().split("from")
            ip = parts[-1].strip()
            failed_attempts[ip] += 1

print("=== Brute Force Detection Report ===\n")

for ip, count in failed_attempts.items():
    if count >= threshold:
        print(f"Suspicious Activity Detected from {ip}")
        print(f"Failed Attempts: {count}\n")
    else:
        print(f"{ip} — Normal Activity ({count} failed attempts)")
