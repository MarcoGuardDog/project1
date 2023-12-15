import requests 
import socket
def ip_public():
    response =  requests.get('https://httpbin.org/ip')
    return response.json()["origin"]

def ip_privad():
    nombre_de_host = socket.gethostname()
    ip_privada = socket.gethostbyname(nombre_de_host)
    return ip_privada 


