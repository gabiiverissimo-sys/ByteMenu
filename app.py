from bottle import Bottle, static_file, run

app = Bottle()

@app.route('/')
def cadastro():
    return static_file('cadastro.html', root='.')

@app.route('/static/<filename:path>')
def serve_static(filename):
    return static_file(filename, root='./static')

if __name__ == "__main__":
    run(app, host='localhost', port=8081, debug=True)