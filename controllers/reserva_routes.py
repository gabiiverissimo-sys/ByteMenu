from bottle import Bottle, get, post, put, delete, request, response
from models.reserva_models import (
    criar_reserva,
    listar_reservas,
    buscar_reserva_por_id,
    atualizar_reserva,
    deletar_reserva
)

reserva_routes = Bottle()

@reserva_routes.post('/reservas')
def nova_reserva():
    data = request.json

    user_id = data.get("user_id")  

    data_reserva = data.get("data")
    horario = data.get("horario")
    num_pessoas = data.get("num_pessoas")
    observacao = data.get("observacao")

    if not user_id or not data_reserva or not horario or not num_pessoas:
        response.status = 400
        return {"erro": "Preencha todos os campos obrigatórios."}

    sucesso = criar_reserva(user_id, data_reserva, horario, num_pessoas, observacao)
    if not sucesso:
        response.status = 500
        return {"erro": "Erro ao criar reserva."}

    return {"msg": "Reserva criada com sucesso!"}


@reserva_routes.get('/reservas')
def listar():
    reservas = listar_reservas()
    return {"reservas": reservas}


@reserva_routes.get('/reservas/<id:int>')
def buscar(id):
    reserva = buscar_reserva_por_id(id)
    if not reserva:
        response.status = 404
        return {"erro": "Reserva não encontrada."}
    return reserva


@reserva_routes.put('/reservas/<id:int>')
def atualizar(id):
    data = request.json
    sucesso = atualizar_reserva(
        id,
        data.get("data"),
        data.get("horario"),
        data.get("num_pessoas"),
        data.get("observacao")
    )
    if not sucesso:
        response.status = 404
        return {"erro": "Reserva não encontrada."}
    return {"msg": "Reserva atualizada com sucesso!"}


@reserva_routes.delete('/reservas/<id:int>')
def deletar(id):
    sucesso = deletar_reserva(id)
    if not sucesso:
        response.status = 404
        return {"erro": "Reserva não encontrada."}
    return {"msg": "Reserva deletada com sucesso!"}

@reserva_routes.post('/reservas')
def nova_reserva():
    try:
        data = request.json
        print("DEBUG /reservas - payload recebido:", data)   


        user_id = data.get("user_id")
        data_reserva = data.get("data")
        horario = data.get("horario")
        num_pessoas = data.get("num_pessoas")
        observacao = data.get("observacao")
        mesa = data.get("mesa")  

        if not user_id or not data_reserva or not horario or not num_pessoas:
            response.status = 400
            return {"erro": "Preencha todos os campos obrigatórios (user_id, data, horario, num_pessoas)."}

        sucesso = criar_reserva(user_id, data_reserva, horario, num_pessoas, observacao)  

        if not sucesso:
            response.status = 500
            return {"erro": "Erro ao criar reserva."}

        return {"msg": "Reserva criada com sucesso!"}

    except Exception as e:
        print("ERRO ao criar reserva:", repr(e))
        response.status = 500
        return {"erro": f"Exceção no servidor: {str(e)}"}

