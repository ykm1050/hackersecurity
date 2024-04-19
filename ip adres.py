import socket

def get_ip():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    return IPAddr

print("Your Computer IP Address is: " + get_ip())