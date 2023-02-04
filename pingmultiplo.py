import os
import time

with open('hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()
    
    for ip in dump:
        print(f"Verificando o ip: {ip}")
        print("-"*60)
        os.system('ping -n 6 {}'.format(ip))
        print("-"*60)
        time.sleep(3)

