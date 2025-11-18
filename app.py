from bottle import Bottle, run
from config import HOST, PORT, DEBUG, RELOADER

from controllers.auth_routes import auth_routes
from controllers.user_routes import user_routes
from controllers.reserva_routes import reserva_routes

app = Bottle()
app.merge(auth_routes)
app.merge(user_routes)
app.merge(reserva_routes)

@app.get('/')
def home():
    return {"msg": "API ByteMenu está rodando!"}

if __name__ == "__main__":
    run(app, host=HOST, port=PORT, debug=DEBUG, reloader=RELOADER)
