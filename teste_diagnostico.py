from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    # Ler o template MANUALMENTE
    template_path = os.path.join('templates', 'index.html')
    with open(template_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    print(f"📄 Conteúdo lido: {len(html_content)} caracteres")
    return html_content

if __name__ == "__main__":
    print("🚀 Template FORÇADO - http://localhost:5000")
    app.run(debug=True, port=5000)