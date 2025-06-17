import socket

with open('Host.txt','r') as file:
    hosts=file.readlines()

with open('ip.txt','w') as output:
    for host in hosts:
        host=host.strip()
        if not host:
            continue
        try:
            ip = socket.gethostbyname(host)
            output.write(f"{ip}\n")
        except socket.gaierror:
            output.write("khong resolve duoc\n")


