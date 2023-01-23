# Escreva a função Python ajustar_estoque() com o seus devidos parâmetros para que
# realize a atualização na coleção produto conforme o script que o DBA passou (na questão)

# var sku = "" // a pessoa informa o sku aqui
# var estoque = 0 // valor a ser informado do novo estoque
# db.produto.update(
# {
# sku: sku
# },
# {
# $inc: estoque
# }
# )

from pymongo import MongoClient


url_conexao = MongoClient(
    'mongodb+srv://cluster0.bhbsfvp.mongodb.net/test',
    username='MockDB',
    password='SQ2qo3ouLeSMn9Je')
    
collection = ("testeDEV")

def colecao(url_conexao, collection):
    conn = MongoClient(url_conexao)
    db = [collection]
    db.produto.find({"nome":"batata"})
    return db

def ajustar_estoque(sku, estoque):
    db = colecao(url_conexao, collection)
    db.produto.update({"id": sku},{"$set": {"nome": estoque}})

ajustar_estoque()