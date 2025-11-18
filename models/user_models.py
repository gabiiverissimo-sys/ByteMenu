from .db import get_connection
import bcrypt

def criar_usuario(nome, telefone, email, senha):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt()).decode()

        cursor.execute(
            "INSERT INTO users (nome, telefone, email, senha) VALUES (?, ?, ?, ?)",
            (nome, telefone, email, senha_hash)
        )

        conn.commit()
        conn.close()
        return True

    except Exception as e:
        print("Erro ao criar usuário:", e)
        return False


def listar_usuarios():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, telefone, email FROM users")
    users = cursor.fetchall()
    conn.close()
    return users


def buscar_usuario_por_email(email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()
    conn.close()
    return user


def buscar_usuario_por_id(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, telefone, email FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user


def atualizar_usuario(user_id, nome=None, telefone=None, email=None):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE users
        SET nome = COALESCE(?, nome),
            telefone = COALESCE(?, telefone),
            email = COALESCE(?, email)
        WHERE id = ?
    """, (nome, telefone, email, user_id))

    conn.commit()
    sucesso = cursor.rowcount > 0
    conn.close()
    return sucesso


def deletar_usuario(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    sucesso = cursor.rowcount > 0
    conn.close()
    return sucesso


def verificar_senha(senha_digitada, senha_hash_bd):
    return bcrypt.checkpw(senha_digitada.encode(), senha_hash_bd.encode())
