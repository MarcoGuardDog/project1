from mongoengine import Document , StringField , IntField, connect, ListField

connect(db="guardDog", host="mongodb://guardDog:zwF32WZt@34.132.52.46:27017/guardDog?connectTimeoutMS=10000&authSource=guardDog&directConnection=true", alias='default')

class Telemetry(Document):
    device_id = StringField()
    ip_publica= StringField()
    ip_privada= StringField()
    interfaces=ListField()

def registrar_device_status(device_id,ip_publica,ip_privada,interfaces):
    """este metodo registra en la base de datos :
    divece_id es un string   ej: "device01"
    ip_publica es un string   ej: "127.0.0.1"
    ip_privada es un string   ej: "198.0.0.100"
    interface es una lista de string  ej:["h1","h2"]
    """
    telemetry = Telemetry()
    telemetry.device_id=device_id
    telemetry.ip_publica=ip_publica
    telemetry.ip_privada=ip_privada
    telemetry.interfaces=interfaces
    telemetry.save()
