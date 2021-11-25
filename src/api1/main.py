
from flask import Flask, json, jsonify, request

ENDPOINT_BASE = "/app1/"

app = Flask(__name__)

@app.route('/', methods =['GET'])
@app.route(ENDPOINT_BASE, methods =['GET'])
def home():
    return "<h1>Home</h1>"

@app.route(ENDPOINT_BASE+"nuevo", methods =['POST'])
def nuevo():
    json_entrada = request.json
    print(json_entrada, type(json_entrada), json_entrada.keys())
    return jsonify(json_entrada)

if __name__ == "__main__":
    app.run(debug=True)