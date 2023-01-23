# Elabore uma modelagem de dados em que os registros estão
# relacionados através de um campo identificador (o id), atendendo as seguintes
# afirmações:

# Goias: id_estado 1
    # Diamantina: id_cidade 1
        # Betania: id_bairro 1
# Paraná: id_estado 2
    # Noronha: id_cidade 2
        # Agostinho: id_bairro 2
        # Natal: id_bairro 3


estado = [
    {"id_estado":1, "estado": "Goiás"},
    {"id_estado":2, "estado": "Paraná"}
    ]

cidade = [
    {"id_cidade":1, "cidade" : "Diamantina"},
    {"id_cidade":2, "cidade" :"Noronha"}
    ]

bairro = [
    {"id_bairro":1, "bairro": "Betania"},
    {"id_bairro":2, "bairro": "Agostinho"},
    {"id_bairro":3, "bairro": "Natal"}
    ]

endereco = [
    {"id_estado":1, "id_cidade":1, "id_bairro":1},
    {"id_estado":2, "id_cidade":2, "id_bairro":2,"id_bairro":3 },
    ]
