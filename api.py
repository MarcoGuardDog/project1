from flask import Flask, jsonify, request 
from modulo_mongo import registrar_device_status


app = Flask(__name__)


@app.route("/send_service_status",methods=["post"])
def send_service_status ():
    data = request.get_json()
    device_id = data.get("device_id",None)
    ip_publica = data.get("ip_publica",None)
    ip_privada = data.get("ip_privada", None)
    interfaces = data.get("interfaces",None)
    if device_id == None or ip_publica == None or ip_privada == None or interfaces == None :
        return jsonify({"message : hay un error "})

    registrar_device_status(device_id,ip_publica,ip_privada,interfaces)

    print(device_id,ip_publica,ip_privada,interfaces)

    return jsonify({"mensaje":"service se registro."})
 
if __name__ == '__main__':
    app.run(debug=True)
