import requests 
import socket
def ip_public():
    response =  requests.get('https://httpbin.org/ip')
    return response.json()["origin"]

def ip_privad():
    nombre_de_host = socket.gethostname()
    ip_privada = socket.gethostbyname(nombre_de_host)
    print(ip_privada) 

print("esta una ip_publica",ip_public())

ip_privad()