from flask import Flask, render_template  

app = Flask(__name__)

@app.route("/")
def home():
    # O Flask vai automaticamente procurar 'index.html' na pasta 'templates/'
    return render_template("index.html")

if __name__ == "__main__":
    print("Byte Menu rodando: http://localhost:5000")
    app.run(debug=True, port=5000)