# Escreva a função obter_colecao_mongodb(url_conexao, colecao) que irá se
# conectar no MogodDB utilizando alguma biblioteca do Python. Ela possui os
# seguintes parâmetros:
# ○ url_conexao: URI de conexão com banco de dados MongoDB, que também
# informa a base de dados (database). Por exemplo: a URI
# `mongodb://localhost/bancoexemplo', é a string de conexão para o banco
# "bancoexemplo" da minha máquina local ("localhost").
# ○ colecao: É o nome da coleção (collection) do MongoDB que estaremos
# acessando com esta função.

from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

url_conexao = MongoClient(
    'mongodb+srv://cluster0.bhbsfvp.mongodb.net/test',
    username='MockDB',
    password='SQ2qo3ouLeSMn9Je')

collection = ("testeDEV")

db = url_conexao['testeDEV']

# @app.route("/")



if __name__ == "__main__":
    app.run(debug=True, port=5000)
