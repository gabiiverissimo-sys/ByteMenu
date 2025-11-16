from bottle import Bottle, static_file, run

app = Bottle()

# Rota principal - serve a página de reserva
@app.route('/')
def reserva():
    return static_file('reserva.html', root='.')

# Rota para arquivos CSS
@app.route('/static/<filename:path>')
def serve_static(filename):
    return static_file(filename, root='./static')

run(app, host='localhost', port=8080, debug=True)