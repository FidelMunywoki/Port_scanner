#pip install colorama
import socket #for connecting
from colorama import init, Fore 

#some colors

init()
GREEN=Fore.GREEN 
RESET=Fore.RESET 
GRAY=Fore.LIGHTBLACK_EX 

#function to determine if the port is open or closed
def is_port_open(host,port):
    """
    determine whether 'host' has the 'port' open
    """
    #creates a new socket
    s=socket.socket()
    try:
        #tries to connect to host using that port
        s.connect((host,port))
        s.settimeout(0.2)
    except:
        #cannot connet ,port closed
        #return false
        return False
    else:
        #connection was established ,port open
        return True 
    
#using the above function and iterating over range of ports
#get the host from the user

host=input('Enter the host: ')
#iterate over ports, from 1 to 1024

for port in range(1,1024):
    if is_port_open(host,port):
        print(f'{GREEN}[+] {host}:{port} is open  {RESET}')
        
    else:
        print(f'{GRAY}[!] {host}:{port} is closed {RESET}',end="\r")
        