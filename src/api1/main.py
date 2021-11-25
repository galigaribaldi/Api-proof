from flask import Flask, json, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS
import models
ENDPOINT_BASE = "/app1/"
codeStatus = {"error":{"error":404},"success": {"success":201}}
app = Flask(__name__)

CORS(app)
cors = CORS(app, resources={
    r"/*":{
        "origins":"*"
    }
})
app.config['MYSQL_HOST'] = 'sql5.freesqldatabase.com'
app.config['MYSQL_USER'] = 'sql5454056'
app.config['MYSQL_PASSWORD'] = 'x2teBpQpXA'
app.config['MYSQL_DB'] = 'sql5454056'
mysql = MySQL(app)

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
        RFC = json_entrada["RFC"]
        response = models.addUser(nombre,apellido,edad, RFC)
        return response
    else:
        return jsonify(codeStatus["error"])
    
@app.route(ENDPOINT_BASE+"consulta", methods =['POST'])
def consulta():
    json_entrada = request.json
    ###Teniendo sólo el RFC
    if "RFC" in list(json_entrada.keys()):
        rfc = json_entrada["RFC"]
        response = models.getUser(rfc)
        return response
    else:
        return jsonify(codeStatus["error"])
    
@app.route(ENDPOINT_BASE+"borrado", methods =['POST'])
def delete():
    json_entrada = request.json
    if "RFC" in list(json_entrada.keys()):
        rfc = json_entrada["RFC"]
        models.deleteUser(rfc)
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
        RFC = json_entrada["RFC"]
        response = models.updateUser(nombre,apellido,edad,RFC)
        return response
    else:
        return jsonify(codeStatus["error"])    
    
if __name__ == "__main__":
    app.run(debug=True)