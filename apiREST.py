from flask import Flask, request

# Crea una instancia de la aplicación Flask
app = Flask(__name__)

# Ruta para el método GET
@app.route('/saludo', methods=['GET'])
def saludo_get():
    return "¡Hola, este es un saludo desde GET!", 200

# Ruta para el método POST
@app.route('/saludo', methods=['POST'])
def saludo_post():
    data = request.json  # Puedes recibir datos en el cuerpo de la solicitud POST
    nombre = data.get("nombre", "invitado")  # Si envías un nombre, lo usará, de lo contrario, "invitado"
    return f"¡Hola, {nombre}, este es un saludo desde POST!", 201

# Ruta para el método PUT
@app.route('/saludo', methods=['PUT'])
def saludo_put():
    data = request.json  # Puedes recibir datos en el cuerpo de la solicitud PUT
    nombre = data.get("nombre", "invitado")
    return f"¡Hola, {nombre}, tu saludo ha sido actualizado con PUT!", 200

# Ruta para el método DELETE
@app.route('/saludo', methods=['DELETE'])
def saludo_delete():
    return "El saludo ha sido eliminado con DELETE", 200

# Ejecuta la aplicación
if __name__ == '__main__':
    app.run(debug=True)
