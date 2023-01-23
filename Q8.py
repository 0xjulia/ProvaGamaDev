# Crie um programa que seja uma API de um contador de números. Esta API irá
# manter o número em sua memória, e esta irá iniciar com o valor 0 (zero).
# Para o programa teremos as seguinte chamadas:
# ● POST /contador
# {
# "numero": <numero>
# }
# Irá definir um novo número para o nosso contador. O método irá retornar um
# HTTP 201.
# ●GET /contador
# Retorna o número que foi guardado na memória, em um JSON no formato:
# {
# "numero": <numero guardado>
# }
# E também um HTTP 200.
# ●PUT /contador/incrementa

# Irá incrementar o valor do número em 1 e retornar um HTTP 202.
# ●DELETE /contador
# Irá zerar o valor do contador. A API irá retornar um HTTP 202.

from flask import Flask, request

app = Flask(__name__)

count = {"count": 0}


@app.post('/contador')
def new_value():
    value = request.get_json('num')
    count["count"] = value['num']
    return "", 201

@app.get('/contador') 
def get_value():
    return {'num': count["count"]},  200

@app.put('/contador/incrementa')
def incrementa():
    count["count"] += 1
    return '', 202

@app.delete('/contador') 
def delete():
    count['count'] = 0
    return '', 202

if __name__ == '__main__':
    app.run(debug=True)