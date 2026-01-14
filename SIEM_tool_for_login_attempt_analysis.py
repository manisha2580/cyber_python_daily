#BASIC SIEM TOOL
failed_logins = [2, 12, 100, 5, 0]
logins =["192.168.1.1", "10.0.0.5", "192.168.1.10", "172.16.0.1", "192.168.1.5"]
threat_count=0
for count, ip in zip(failed_logins, logins):
    if count>=100:
        print(f"count id {count}, ALERT SYSTEM NEEDS TO SHUTDOWN")
        threat_count+=1
    elif count >= 20:
        print(f"num of attempt {count}, status is HIGH PRIORITY")
        threat_count+=1
    elif count >= 10:
        print(f"num of attempt {count}, status is SUSPICIOUS")
        threat_count+=1
    elif count<=3:
        print(f"num {count}, status is LOW PRIORITY")
    elif count == 0:
        print(f"num {count}, status is SAFE")
    else:
        print(f"num {count}, ALERT SYSTEM NEEDS TO SHUTDOWN")
        threat_count+=1

    if ip.startswith("192"):
        print(f"INTERNAL IP {ip}")
    else:
        print(f"EXTERNAL IP {ip}")
print("*"*100)
print(f"TOTAL NUMBER OF THREATS ARE {threat_count}")

if threat_count>=2:
    print(f"ACTION REQUIRED")


