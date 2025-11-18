from bottle import Bottle, get, post, put, delete, request, response
from models.user_models import (
    criar_usuario,
    listar_usuarios,
    buscar_usuario_por_id,
    atualizar_usuario,
    deletar_usuario
)

user_routes = Bottle() 

#criar usuário
@user_routes.post('/usuarios')
def registrar_usuario():
    data = request.json

    nome = data.get("nome")
    telefone = data.get("telefone")
    email = data.get("email")
    senha = data.get("senha")

    if not nome or not email or not senha:
        response.status = 400
        return {"erro": "Preencha todos os campos obrigatórios."}

    sucesso = criar_usuario(nome, telefone, email, senha)

    if not sucesso:
        response.status = 409
        return {"erro": "E-mail já registrado."}

    return {"msg": "Usuário criado com sucesso!"}


#listar
@user_routes.get('/usuarios')
def listar():
    users = listar_usuarios()
    return {"usuarios": [dict(u) for u in users]}


#buscar
@user_routes.get('/usuarios/<id:int>')
def buscar(id):
    user = buscar_usuario_por_id(id)
    if not user:
        response.status = 404
        return {"erro": "Usuário não encontrado."}
    return dict(user)


#atualizar
@user_routes.put('/usuarios/<id:int>')
def atualizar(id):
    data = request.json
    nome = data.get("nome")
    telefone = data.get("telefone")
    email = data.get("email")

    sucesso = atualizar_usuario(id, nome, telefone, email)
    if not sucesso:
        response.status = 404
        return {"erro": "Usuário não encontrado."}

    return {"msg": "Usuário atualizado com sucesso!"}


#deletar
@user_routes.delete('/usuarios/<id:int>')
def deletar(id):
    sucesso = deletar_usuario(id)
    if not sucesso:
        response.status = 404
        return {"erro": "Usuário não encontrado."}

    return {"msg": "Usuário deletado com sucesso!"}
