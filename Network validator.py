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
print("*"*1000)
print("updated")
server_ports = {80: "CLOSED", 443: "CLOSED", 22: "OPEN", 21: "OPEN", 3389: "CLOSED"}    # SSH (High Risk if not managed!)       # FTP (Very Old/Unsafe)
services = {22: "SSH", 21: "FTP", 80: "HTTP"}
logins = ["192.168.1.1", "10.0.0.5", "192.168.1.10", "172.16.0.1", "192.168.1.5"]
print("******* STARTING NETWORK AUDIT *******")
def network_audit():
    for i in server_ports:
        status=server_ports[i]
        name=services.get(i,"UNKNOWN")
        if status=="OPEN":
            print(f"Open port is {i} and Network service is {name}")
print("******* IP Masking *******")
def ip_masking():
    for ip in logins:
        split = ip.split(".")
        split[2]="*"
        split[3]="*"
        joint=".".join(split)
        print(joint)

check1=network_audit(), ip_masking()
print(check1)


