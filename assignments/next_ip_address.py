# next 5 ip address
import ipaddress
ip = "192.168.255.252"
start_ip = ipaddress.IPv4Address(int(ipaddress.IPv4Address(ip))+1)
end_ip = ipaddress.IPv4Address(int(ipaddress.IPv4Address(ip))+6)
for i in range(int(start_ip),int(end_ip)):
    # print(ipaddress.IPv4Address(i))
    ip_dot = str(ipaddress.IPv4Address(i))
    ip_space = ip_dot.replace(".", " ")
    print(ip_space)
