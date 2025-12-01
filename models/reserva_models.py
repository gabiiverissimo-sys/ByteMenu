from .db import get_connection
from datetime import datetime

def criar_reserva(user_id, data, horario, num_pessoas, observacao=None):
    try:
        # tenta converter data dd/mm/yyyy
        try:
            data_iso = datetime.strptime(data, "%d/%m/%Y").strftime("%Y-%m-%d")
        except ValueError:
            # tenta converter yyyy-mm-dd
            data_iso = datetime.strptime(data, "%Y-%m-%d").strftime("%Y-%m-%d")

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO reservas (user_id, data, horario, num_pessoas, observacao)
            VALUES (?, ?, ?, ?, ?)
        """, (user_id, data_iso, horario, num_pessoas, observacao))
        
        conn.commit()
        conn.close()
        return True

    except Exception as e:
        print("Erro ao criar reserva:", type(e).__name__, e)
        return False



def listar_reservas():
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT r.id, r.data, r.horario, r.num_pessoas, r.observacao,
               u.nome, u.telefone
        FROM reservas r
        JOIN users u ON r.user_id = u.id
    """)
    reservas = cursor.fetchall()
    conn.close()

    # converter data para DD/MM/YYYY - facilitar leitura
    resultado = []
    for r in reservas:
        reserva_dict = dict(r)
        reserva_dict["data"] = datetime.strptime(reserva_dict["data"], "%Y-%m-%d").strftime("%d/%m/%Y")
        resultado.append(reserva_dict)

    return resultado


def buscar_reserva_por_id(reserva_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT r.id, r.data, r.horario, r.num_pessoas, r.observacao,
               u.nome, u.telefone
        FROM reservas r
        JOIN users u ON r.user_id = u.id
        WHERE r.id = ?
    """, (reserva_id,))
    reserva = cursor.fetchone()
    conn.close()

    if reserva:
        reserva_dict = dict(reserva)
        reserva_dict["data"] = datetime.strptime(reserva_dict["data"], "%Y-%m-%d").strftime("%d/%m/%Y")
        return reserva_dict
    return None


def atualizar_reserva(reserva_id, data=None, horario=None, num_pessoas=None, observacao=None):
    conn = get_connection()
    cursor = conn.cursor()

    if data:
        data = datetime.strptime(data, "%d/%m/%Y").strftime("%Y-%m-%d")

    cursor.execute("""
        UPDATE reservas
        SET data = COALESCE(?, data),
            horario = COALESCE(?, horario),
            num_pessoas = COALESCE(?, num_pessoas),
            observacao = COALESCE(?, observacao)
        WHERE id = ?
    """, (data, horario, num_pessoas, observacao, reserva_id))

    conn.commit()
    sucesso = cursor.rowcount > 0
    conn.close()
    return sucesso


def deletar_reserva(reserva_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM reservas WHERE id = ?", (reserva_id,))
    conn.commit()
    sucesso = cursor.rowcount > 0
    conn.close()
    return sucesso
