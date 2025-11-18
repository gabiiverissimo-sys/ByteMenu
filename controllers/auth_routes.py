from bottle import Bottle, request, response
from models.user_models import (
    criar_usuario,
    buscar_usuario_por_email,
    verificar_senha
)

auth_routes = Bottle()

#cadastro - publico
@auth_routes.post('/register')
def register():
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

    return {"mensagem": "Usuário criado com sucesso!"}


#login
@auth_routes.post('/login')
def login():
    data = request.json

    email = data.get("email")
    senha = data.get("senha")

    user = buscar_usuario_por_email(email)

    if not user:
        response.status = 404
        return {"erro": "Usuário não encontrado."}

    if not verificar_senha(senha, user["senha"]):
        response.status = 401
        return {"erro": "Senha incorreta."}

    return {
        "mensagem": "Login realizado com sucesso!",
        "user": {
            "id": user["id"],
            "nome": user["nome"],
            "email": user["email"]
        }
    }
