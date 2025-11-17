from bottle import Bottle, run, static_file

app = Bottle()

# menu - inicial
@app.route('/')
def menu():
    return static_file('menu.html', root='./views')

#login
@app.route('/login')
def login():
    return static_file('login.html', root='./views')

#cadastro
@app.route('/cadastro')
def cadastro():
    return static_file('cadastro.html', root='./views')

#reserva
@app.route('/reserva')
def reserva():
    return static_file('reserva.html', root='./views')

@app.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')

if __name__ == '__main__':
    print("Byte Menu rodando em: http://localhost:5000")
    run(app, host='localhost', port=5000, debug=True, reloader=True)
