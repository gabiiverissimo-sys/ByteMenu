from bottle import Bottle, run, static_file, template

app = Bottle()

@app.route('/')
def home():
    return template('index.html')

@app.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')

if __name__ == '__main__':
    print("Byte Menu rodando: http://localhost:5000")
    run(app, host='localhost', port=5000, debug=True, reloader=True)
