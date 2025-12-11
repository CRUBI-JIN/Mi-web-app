from flask_restful import Resource

from flask import make_response, render_template
# Vamos a crear recursos -> Para nosotros poder crear recursos
# lo haremos a través de clases y objetos}
class HolaMundo(Resource):
    # Los recursos van a poder ejecutar dos acciónes  -> métodos
    def get(self):
        return {"hola": "hola mundo"}

class PantallaInicio(Resource):
    def get(self):

        # Renderizamos el contenido del archivo html
        contenido = render_template("index.html")

        # Retornamos el contenido renderizado en una respueta
        return make_response(contenido)

class Despedida(Resource):
    def get(self):
        return "Adios"