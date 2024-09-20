from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_URL = "https://xxxxxxxxxxxxxxxxxxx.mockapi.io/api/v1/IoTCarStatus"

# Obtener todos los registros
@app.route('/status', methods=['GET'])
def get_all_status():
    response = requests.get(API_URL)
    return jsonify(response.json()), response.status_code

# Obtener un registro por ID
@app.route('/status/<int:id>', methods=['GET'])
def get_status_by_id(id):
    response = requests.get(f"{API_URL}/{id}")
    return jsonify(response.json()), response.status_code

# Crear un nuevo registro
@app.route('/status', methods=['POST'])
def create_status():
    data = request.json
    response = requests.post(API_URL, json=data)
    return jsonify(response.json()), response.status_code

# Actualizar un registro por ID
@app.route('/status/<int:id>', methods=['PUT'])
def update_status(id):
    data = request.json
    response = requests.put(f"{API_URL}/{id}", json=data)
    return jsonify(response.json()), response.status_code

# Eliminar un registro por ID
@app.route('/status/<int:id>', methods=['DELETE'])
def delete_status(id):
    response = requests.delete(f"{API_URL}/{id}")
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
