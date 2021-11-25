from flask import Flask, json, jsonify, request

ENDPOINT_BASE = "/app1/"
codeStatus = {"error":{"error":404},"success": {"success":201}}
app = Flask(__name__)

@app.route('/', methods =['GET'])
@app.route(ENDPOINT_BASE, methods =['GET'])
def home():
    return "<h1>Home</h1>"

########################################
############# Endpoints ################
########################################

@app.route(ENDPOINT_BASE+"registro", methods =['POST'])
def registro():
    json_entrada = request.json
    claves = list(json_entrada.keys())
    if "RFC" in claves:
        nombre = json_entrada["nombre"] if "nombre" in claves else ""
        apellido = json_entrada["apellido"] if "apellido" in claves else ""
        edad = json_entrada["edad"] if "edad" in claves else ""
        return jsonify(json_entrada)
    else:
        return jsonify(codeStatus["error"])
    
@app.route(ENDPOINT_BASE+"consulta", methods =['POST'])
def consulta():
    json_entrada = request.json
    ###Teniendo sólo el RFC
    if "RFC" in list(json_entrada.keys()):
        rfc = json_entrada["RFC"]
        return jsonify(codeStatus["success"])
    else:
        return jsonify(codeStatus["error"])
    
@app.route(ENDPOINT_BASE+"borrado", methods =['POST'])
def delete():
    json_entrada = request.json
    if "RFC" in list(json_entrada.keys()):
        rfc = json_entrada["RFC"]
        return jsonify(codeStatus["success"])
    else:
        return jsonify(codeStatus["error"])
    
@app.route(ENDPOINT_BASE+"update", methods =['POST'])
def update():
    json_entrada = request.json
    claves = list(json_entrada.keys())
    if "RFC" in claves:
        nombre = json_entrada["nombre"] if "nombre" in claves else ""
        apellido = json_entrada["apellido"] if "apellido" in claves else ""
        edad = json_entrada["edad"] if "edad" in claves else ""
        return jsonify(json_entrada)
        #return jsonify(codeStatus["success"])
    else:
        return jsonify(codeStatus["error"])    
    
if __name__ == "__main__":
    app.run(debug=True)