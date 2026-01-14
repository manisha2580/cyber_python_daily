# Project: Internal Network Validator
# Objective: Identify unauthorized external IP addresses in server logs

logins = ["192.168.1.1", "10.0.0.5", "192.168.1.10", "172.16.0.1", "192.168.1.5"]

print("--- INITIALIZING NETWORK SCAN ---")

for ip in logins:
    if ip.startswith("192"):
        print(f"[OK] {ip} is an internal, authorized address.")
    else:
        print(f"[!!] ALERT: {ip} is EXTERNAL. Flagged for investigation.")

print("--- SCAN COMPLETE ---")
