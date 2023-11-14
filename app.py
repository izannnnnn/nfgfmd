#Importar el módulo Flask en el proyecto.
from flask import Flask,render_template

#Crear un objeto de la clase Flask.
app = Flask(__name__)


#La función route() de la clase Flask.
@app.route("/")
def home():
    name="izan"
    age="15"
    return render_template("index.html",name=name,age=age)
def ma():
    name="greta"
    age="38"
    return render_template("ma.html",name=name,age=age)
def pa():
    name="gonzalo"
    age="42"
    return render_template("pa.html",name=name,age=age)
def amigo():
    name="sergio"
    age="15"
    return render_template("amigo.html",name=name,age=age)  

#‘/’ URL está vinculado con la función first_flask.
def first_flask():

    return "Este es mi primer programa en Flask"

#Ejecutamos la app en el servidor local.
app.run()
