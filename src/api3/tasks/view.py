from flask import Blueprint, request, jsonify
from api3.tasks.models.Task import Task
import api3.tasks.dao as dao
enp1 = Blueprint('end1', __name__)

@enp1.route('/')
@enp1.route('/home', methods = ['POST', 'GET'])
def home():
    json_entrada = request.json
    print(json_entrada)
    return "home"

@enp1.route('/crea_tarea')
def crea_tarea():
    json_entrada = request.json
    if 'description' and 'duration' and 'time_registred' in list(json_entrada.keys()):
        c = dao.insert(json_entrada["description"],
                json_entrada["duration"],
                json_entrada["time_registred"],
                json_entrada["status"],
                json_entrada["id"]
                )
        return jsonify({"success":00, "descirption":str(c)+ " Complete!"})
    else:
        return jsonify({"fail": 201})

@enp1.route('/modifica_tarea')
def modifica_tarea():
    json_entrada = request.json
    if 'description' and 'duration' and 'time_registred' in list(json_entrada.keys()):
        c = dao.update(json_entrada["description"],
                json_entrada["duration"],
                json_entrada["time_registred"],
                json_entrada["status"],
                json_entrada["id"]
                )
        if type(c) == str:
            return jsonify({"fail": 201, "descprition":c})
        return jsonify({"success":00})
    else:
        return jsonify({"fail": 201})

@enp1.route('/elimina_tarea')
def elimina_tarea():
    json_entrada = request.json
    if 'id' in list(json_entrada.keys()):
        c = dao.delete(json_entrada["id"])
        return jsonify({"success":00, "description": str(c)})
    else:
        return jsonify({"fail": 201, "description":"Fallo en eliminarse"})

@enp1.route('/get_by_status')
def get_by_status():
    json_entrada = request.json
    if 'status' in list(json_entrada.keys()):
        c = dao.get_by_status(json_entrada["status"])
        c = [str(x) for x in c]
        return jsonify({"success":00,"Lista": c})
    else:
        return jsonify({"fail": 201, "description":"Fallo en eliminarse"})

@enp1.route('/get_by_description')
def tareas_cadena():
    json_entrada = request.json
    if 'description' in list(json_entrada.keys()):
        c = dao.get_by_description(json_entrada["description"])
        c = [str(x) for x in c]
        return jsonify({"success":00,"Lista": c})
    else:
        return jsonify({"fail": 201, "description":"Fallo en eliminarse"})