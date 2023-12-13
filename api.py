from flask import Flask, jsonify, request 


app = Flask(__name__)


@app.route("/tele",methods=["post"])
def send_tele():
    data = request.get_json()
    
    device_id = data.get("device_id",None)
    ip_publica = data.get("ip_publica",None)
    ip_privada =data.get("ip_privada", None)
    interfaces= data.get("interfaces",None)

    


    print(device_id,ip_publica,ip_privada,interfaces)

    return jsonify({"mensaje":"tele inviada"})



  
if __name__ == '__main__':
    app.run(debug=True)





