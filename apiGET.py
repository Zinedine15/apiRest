from flask import Flask

# Crea una instancia de la aplicación Flask
app = Flask(__name__)

# Define una ruta para la API
@app.route('/saludo', methods=['GET'])
def saludo():
    return "¡Hola, bienvenido a la API!", 200

# Ejecuta la aplicación
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask

# Crea una instancia de la aplicación Flask
app = Flask(__name__)

# Define una ruta para la API
@app.route('/saludo', methods=['GET'])
def saludo():
    return "¡Hola, bienvenido a la API!", 200

# Ejecuta la aplicación
if __name__ == '__main__':
    app.run(debug=True)
