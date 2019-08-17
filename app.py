from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

postagens = [
    {
        "codigo": "1",
        "titulo": "Python é muito legal",
        "corpo": "Test test test test test test test test test test test test test test..."
    },
    {
        "codigo": "2",
        "titulo": "Vue é sensacional!!!",
        "corpo": ".. test test test test test test test test test test test test test test test test..."
    },
    {
        "codigo": "3",
        "titulo": "Python + Vue = <3",
        "corpo": "... test test test test test test test test test test test test test test."
    }
]

class Postagem(Resource):
    def get(self, codigo):
        for postagem in postagens:
            if(codigo == postagem["codigo"]):
                return postagem, 200
        return "Postagem não encontrada", 404

    def post(self, codigo):
        parser = reqparse.RequestParser()
        parser.add_argument("titulo")
        parser.add_argument("corpo")
        args = parser.parse_args()

        for postagem in postagens:
            if(codigo == postagem["codigo"]):
                return "Postagem com ID {} já existe".format(codigo), 400

        postagem = {
            "id": codigo,
            "titulo": args["titulo"],
            "corpo": args["corpo"]
        }
        postagens.append(postagem)
        return postagem, 201

    def put(self, codigo):
        parser = reqparse.RequestParser()
        parser.add_argument("titulo")
        parser.add_argument("corpo")
        args = parser.parse_args()

        for postagem in postagens:
            if(id == postagem["codigo"]):
                postagem["titulo"] = args["titulo"]
                postagem["corpo"] = args["corpo"]
                return postagem, 200
        
        postagem = {
            "id": codigo,
            "titulo": args["titulo"],
            "corpo": args["corpo"]
        }
        postagens.append(postagem)
        return postagem, 201

    def delete(self, codigo):
        global postagens
        postagens = [postagem for postagem in postagens if postagem["codigo"] != codigo]
        return "{} is deleted.".format(codigo), 200
      
api.add_resource(Postagem, "/postagem/<string:codigo>")

app.run(debug=True)

