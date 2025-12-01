from bottle import Bottle, request, response
from models.user_models import (
    criar_usuario,
    buscar_usuario_por_email,
    verificar_senha,
    deletar_usuario
)
import jwt
from datetime import datetime, timedelta
from config import SECRET_KEY, JWT_ALGORITHM, JWT_EXP_HOURS 

auth_routes = Bottle()

def autenticar():
    token = request.get_header("Authorization")

    if not token:
        response.status = 401
        return {"erro": "Token não fornecido."}

    try:
        token = token.replace("Bearer ", "")
        dados = jwt.decode(token, SECRET_KEY, algorithms=[JWT_ALGORITHM]) 
        return dados  
    except jwt.ExpiredSignatureError:
        response.status = 401
        return {"erro": "Token expirado."}
    except Exception as e:
        print(f"Erro ao decodificar token: {e}") 
        response.status = 401
        return {"erro": "Token inválido."}

#teste de rota
@auth_routes.get('/login')
def login_info():
    return {"info": "Use POST /login para fazer login com email e senha."}

#cadastro de usuário
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


#login de usuário
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

    #geração do token JWT
    token = jwt.encode(
        {
            "user_id": user["id"],
            "exp": datetime.utcnow() + timedelta(hours=JWT_EXP_HOURS) 
        },
        SECRET_KEY, 
        algorithm=JWT_ALGORITHM 
    )

    return {
        "mensagem": "Login realizado com sucesso!",
        "token": token,
        "user": {
            "id": user["id"],
            "nome": user["nome"],
            "email": user["email"]
        }
    }

#deletar conta - uso de token JWT
@auth_routes.delete('/user/delete')
def deletar_conta():
    auth = autenticar()
    if isinstance(auth, dict) and "erro" in auth:
        return auth  # token inválido

    user_id = auth["user_id"]

    sucesso = deletar_usuario(user_id)

    if not sucesso:
        response.status = 500
        return {"erro": "Erro ao deletar conta."}

    return {"mensagem": "Conta deletada com sucesso!"}