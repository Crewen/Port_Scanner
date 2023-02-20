#!/usr/bin/python3

import socket
import sys
import pyfiglet
import threading


ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

usage = "python3 port_scanner.py IP_ADDRESS START_PORT END_PORT" 

if(len(sys.argv)!=4):
    print(usage)
    sys.exit()


address =socket.gethostbyname(sys.argv[1])  

start_port = int(sys.argv[2])
end_port = int(sys.argv[3])


print("-"*100)
print("Scanning ip: " + address)
print("-"*100)


try:
    
    def scan_port(port):
        print("Scanning port: ",port)
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        #result
        result = s.connect_ex((address,port))
        if result ==0:
            print("[*] Port {} is open".format(port))
        s.close()  

    for port in range (start_port,end_port+1):                           

        thread= threading.Thread( target= scan_port, args= (port,))  
        thread.start()

except KeyboardInterrupt:
    print("\n Exiting...!!")
    sys.exit() 

except socket.error:

     print("/n Not Responding..! ")
     sys.exit()
               


