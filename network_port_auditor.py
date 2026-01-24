server_ports = {80: "CLOSED", 443: "CLOSED", 22: "OPEN", 21: "OPEN", 3389: "CLOSED"}    # SSH (High Risk if not managed!)       # FTP (Very Old/Unsafe)
services = {22: "SSH", 21: "FTP", 80: "HTTP"}
for i in server_ports:
    status=server_ports[i]
    name=services.get(i,"UNKNOWN")
    if status=="OPEN":
        print(f"port is{i}  open and service is  is {name}")
