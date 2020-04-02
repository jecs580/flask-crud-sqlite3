"""Main"""
# Flask
from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////database/task.db'  # Conexion con una base de datos.
db = SQLAlchemy(app)  # Crea una instacia de SQLAlchemy para manejar el ORM
# ROUTERS
@app.route('/')
#  Ruta raiz
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)  # Colocamos degug = True para que nuestro servidor se reinicia cada vez que guardamos cambios
    