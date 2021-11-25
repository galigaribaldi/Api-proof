from flask import Flask, json, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS

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

def addUser(nombre,apellido,edad,RFC):
    conect = mysql.connection.cursor()
    conect.execute('INSERT INTO persona(nombre,apellido,edad,RFC) VALUES (%s,%s,%s,%s)',(nombre,apellido,edad,RFC))
    conect.execute('SELECT * FROM persona WHERE RFC=%s',(RFC,))
    data = conect.fetchall()
    if (data):
        columns=[x[0] for x in conect.description]
        conect.close()
        json_data=[]
        for result in data:
            json_data.append(dict(zip(columns,result)))
        return jsonify(json_data)
    else:
        json_data=[]
        return jsonify(json_data)

def getUser(RFC):
    conect = mysql.connection.cursor()
    conect.execute('SELECT * FROM persona WHERE RFC=%s',(RFC,))
    data = conect.fetchall()
    if (data):
        columns=[x[0] for x in conect.description]
        conect.close()
        json_data=[]
        for result in data:
            json_data.append(dict(zip(columns,result)))
        return jsonify(json_data)
    else:
        json_data=[]
        return jsonify(json_data)

def deleteUser(RFC):
    conect = mysql.connection.cursor()
    conect.execute('DELETE FROM persona WHERE RFC=%s',(RFC,))
    data = conect.fetchall()
    if (data):
        columns=[x[0] for x in conect.description]
        conect.close()
        json_data=[]
        for result in data:
            json_data.append(dict(zip(columns,result)))
        return jsonify(json_data)
    else:
        json_data=[]
        return jsonify(json_data)

def updateUser(nombre,apellido,edad,RFC):
    conect = mysql.connection.cursor()
    conect.execute('UPDATE persona set nombre=%s, apellido=%s, edad=%s,RFC=%s WHERE RFC=%s',(nombre,apellido,edad,RFC,RFC))
    conect.execute('SELECT * FROM persona WHERE RFC=%s',(RFC,))
    data = conect.fetchall()
    if (data):
        columns=[x[0] for x in conect.description]
        conect.close()
        json_data=[]
        for result in data:
            json_data.append(dict(zip(columns,result)))
        return jsonify(json_data)
    else:
        json_data=[]
        return jsonify(json_data)