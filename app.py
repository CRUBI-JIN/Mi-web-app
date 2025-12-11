#Desde la librería "Flask"
#vamos a importar la clase Falsk

from flask import Flask

# Desde flask_restful importamos la clase API  y la clase
# Resource

from flask_restful import Api, Resource
from rutas import crear_rutas

# Vamos a crear un objeto de tipo "Flask"
app = Flask(__name__)


# Creamos un objeto de tipo API y como argumento
# le pasamos el objeto app
api = Api(app)

crear_rutas(api)

# La API será  el programa que se comunique con el dispositivo físico





#   Del objeto app ejecutamos el método run

app.run(port=8080, debug=True)

#127.0.0.1 -> LoopBack | (IP LOCAL)