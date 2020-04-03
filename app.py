"""Main"""
# Flask
from flask import Flask, render_template,request

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/tasks.db'  # Conexion con una base de datos.
db = SQLAlchemy(app)  # Crea una instacia de SQLAlchemy para manejar el ORM
# ROUTERS
class Task(db.Model):
    """Modelo de Tarea."""
    id=db.Column(db.Integer,primary_key=True)
    content=db.Column(db.String(200))
    done= db.Column(db.Boolean)

@app.route('/')
#  Ruta raiz
def hello_world():
    return render_template('index.html')  # Colocamos entre comillas simples el nombre del archivo html
    # Por defecto Flask buscara las plantillas en la carpeta de nombre templates que este al nivel del archivo controlador(app.py)

@app.route('/create-task',methods=['POST'])
def create():
    """Crear Tareas"""
    task = Task(content=request.form['tarea'], done=False)
    db.session.add(task)  # Agregamos un nuevo dato a la base de datos.
    db.session.commit()  # Terminamos la consulta y guarda el dato
    return 'guardado'  # Devolvemos una respuesta al navegador con el mensaje 'guardado'


if __name__ == '__main__':
    app.run(debug=True)  # Colocamos degug = True para que nuestro servidor se reinicia cada vez que guardamos cambios
    