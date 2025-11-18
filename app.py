from bottle import Bottle, run
from config import HOST, PORT, DEBUG, RELOADER

from controllers.auth_routes import auth_routes
from controllers.user_routes import user_routes

app = Bottle()
app.merge(auth_routes)
app.merge(user_routes)

@app.get('/')
def home():
    return {"msg": "API ByteMenu está rodando! Use /usuarios, /register ou /login."}

if __name__ == "__main__":
    run(app, host=HOST, port=PORT, debug=DEBUG, reloader=RELOADER)
