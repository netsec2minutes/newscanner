import sys
import socket
import ipaddress
from datetime import datetime
from datetime import date
print("SCANNER")
print(".......................")
iprange = input("Adicione o Range de Rede?  ")
iprangenetwork=ipaddress.ip_network(iprange)
beginport = int(input("O Range é iniciado na porta?  "))
finalport = int(input("Até a Porta?  "))
empresa = input("Digite o nome da empresa:  ")
data_atual = date.today()
data=data_atual.strftime('%d-%m-%Y')
output = "Relatório-"+str(empresa)+"-"+str(data)
print("-" * 50)
print("Scan Alvo:  " + iprange)
print("-" * 50)
sys.stdout = open(output, "w")
print("Iniciado em :" + str(datetime.now()))
for x in iprangenetwork.hosts():
    target=0
    s=0
    target = ipaddress.ip_address(x)
    strtarget=str(target)
    print("Scan para o Server: " + strtarget)
    for port in range(beginport,finalport):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((strtarget,port))
        if result ==0:
            print("Port {} está aberta".format(port))
            s.close()
        
print("Finalizado em :" + str(datetime.now()))
sys.stdout.close()
© 2021 GitHub, Inc.
Terms
Priv
