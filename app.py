from bottle import Bottle, run, response, request
from config import HOST, PORT, DEBUG, RELOADER

from controllers.auth_routes import auth_routes
from controllers.user_routes import user_routes
from controllers.reserva_routes import reserva_routes

app = Bottle()

@app.hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:5000'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, Authorization'
    response.headers['Access-Control-Allow-Credentials'] = 'true'

@app.route('/<:re:.*>', method='OPTIONS')
def options_handler():
    return {}

app.merge(auth_routes)
app.merge(user_routes)
app.merge(reserva_routes)

@app.get('/')
def home():
    return {"msg": "API ByteMenu está rodando!"}

if __name__ == "__main__":
    print(f"Backend rodando em http://{HOST}:{PORT}")
    run(app, host=HOST, port=PORT, debug=DEBUG, reloader=RELOADER)
