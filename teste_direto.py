from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    # Teste DIRETO - sem usar render_template
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>TESTE ULTRA SIMPLES</title>
        <meta charset="UTF-8">
    </head>
    <body style="background: purple; color: white; text-align: center; padding: 100px;">
        <h1>🟣 PAGINA ROXA</h1>
        <p>Se você vê ROXO, o problema é no render_template()</p>
        <p>Se vê BRANCO, o problema é no seu navegador/sistema</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    print("🎯 Teste ULTRA SIMPLES - http://localhost:5000")
    app.run(debug=True, port=5000)