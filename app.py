from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Byte Menu - Cardápio</title>
        <meta charset="UTF-8">
        <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Playfair+Display:wght@700&display=swap" rel="stylesheet">
        <style>
            body {
                background: #6a1b1b;
                color: white;
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
            }
            .header {
                background: #3e2723;
                padding: 2rem;
                text-align: center;
                border-bottom: 4px solid #c89b3c;
            }
            .logo {
                color: #c89b3c;
                font-size: 3rem;
                margin-bottom: 0.5rem;
                font-family: 'Cinzel', serif;
                font-weight: 700;
                letter-spacing: 2px;
                text-transform: uppercase;
            }
            .menu-container {
                max-width: 800px;
                margin: 2rem auto;
                padding: 0 1rem;
            }
            .categoria {
                margin: 2rem 0;
            }
            .categoria-titulo {
                color: #c89b3c;
                font-size: 1.8rem;
                border-bottom: 2px solid #c89b3c;
                padding-bottom: 0.5rem;
                margin-bottom: 1rem;
            }
            .card {
                background: white;
                color: black;
                padding: 1.5rem;
                margin: 1rem 0;
                border-radius: 10px;
                border-left: 5px solid #c89b3c;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            }
            .prato-nome {
                color: #6a1b1b;
                font-size: 1.3rem;
                margin: 0 0 0.5rem 0;
                font-weight: bold;
            }
            .prato-descricao {
                color: #666;
                margin: 0 0 1rem 0;
                font-style: italic;
            }
            .prato-preco {
                color: #25d366;
                font-size: 1.4rem;
                font-weight: bold;
                text-align: right;
                margin: 0;
            }
            .footer {
                background: #3e2723;
                text-align: center;
                padding: 1.5rem;
                margin-top: 3rem;
                border-top: 2px solid #c89b3c;
            }
        </style>
    </head>
    <body>
        <div class="header">
            <div class="logo">Byte Menu</div>
            <p>Cardápio Digital</p>
        </div>

        <div class="menu-container">
            <!-- ENTRADAS -->
            <div class="categoria">
                <h2 class="categoria-titulo">Entradas</h2>
                
                <div class="card">
                    <div class="prato-nome">Bruschetta Italiana</div>
                    <p class="prato-descricao">Pão italiano com tomate fresco e manjericão</p>
                    <div class="prato-preco">R$ 30,00</div>
                </div>

                <div class="card">
                    <div class="prato-nome">Carpaccio de Filé Mignon</div>
                    <p class="prato-descricao">Finas fatias de filé mignon com rúcula e parmesão</p>
                    <div class="prato-preco">R$ 50,00</div>
                </div>

                <div class="card">
                    <div class="prato-nome">Salada de Burrata</div>
                    <p class="prato-descricao">Burrata cremosa com tomates heirloom e pesto</p>
                    <div class="prato-preco">R$ 65,00</div>
                </div>

                <div class="card">
                    <div class="prato-nome">Antipasto Italiano</div>
                    <p class="prato-descricao">Seleção de salames, queijos e azeitonas</p>
                    <div class="prato-preco">R$ 25,00</div>
                </div>

                <div class="card">
                    <div class="prato-nome">Polenta Cremosa com Funghi</div>
                    <p class="prato-descricao">Polenta com cogumelos salteados e parmesão</p>
                    <div class="prato-preco">R$ 55,00</div>
                </div>
            </div>

            <!-- PRATOS PRINCIPAIS -->
            <div class="categoria">
                <h2 class="categoria-titulo">Pratos Principais</h2>
                
                <div class="card">
                    <div class="prato-nome">Risoto de Camarão</div>
                    <p class="prato-descricao">Risoto cremoso com camarões frescos</p>
                    <div class="prato-preco">R$ 89,00</div>
                </div>

                <div class="card">
                    <div class="prato-nome">Filé Mignon ao Molho Madeira</div>
                    <p class="prato-descricao">Filé mignon ao molho madeira com arroz à piamontese</p>
                    <div class="prato-preco">R$ 109,00</div>
                </div>

                <div class="card">
                    <div class="prato-nome">Spaghetti à Carbonara</div>
                    <p class="prato-descricao">Massa spaghetti com molho carbonara tradicional</p>
                    <div class="prato-preco">R$ 72,00</div>
                </div>

                <div class="card">
                    <div class="prato-nome">Nhoque com Molho Funghi</div>
                    <p class="prato-descricao">Nhoque com molho de cogumelos porcini frescos</p>
                    <div class="prato-preco">R$ 79,00</div>
                </div>

                <div class="card">
                    <div class="prato-nome">Risoto com Osso Buco</div>
                    <p class="prato-descricao">Risoto cremoso acompanhado de osso buco</p>
                    <div class="prato-preco">R$ 82,00</div>
                </div>
            </div>

            <!-- SOBREMESAS -->
            <div class="categoria">
                <h2 class="categoria-titulo">Sobremesas</h2>
                
                <div class="card">
                    <div class="prato-nome">Tiramisu</div>
                    <p class="prato-descricao">Clássica sobremesa italiana com café e mascarpone</p>
                    <div class="prato-preco">R$ 27,00</div>
                </div>

                <div class="card">
                    <div class="prato-nome">Panna Cotta</div>
                    <p class="prato-descricao">Sobremesa italiana cremosa com calda de frutas vermelhas</p>
                    <div class="prato-preco">R$ 29,00</div>
                </div>

                <div class="card">
                    <div class="prato-nome">Petit Gateau</div>
                    <p class="prato-descricao">Bolinho de chocolate com sorvete de baunilha</p>
                    <div class="prato-preco">R$ 27,00</div>
                </div>

                <div class="card">
                    <div class="prato-nome">Cannoli Siciliano</div>
                    <p class="prato-descricao">Tubos crocantes recheados com ricota doce</p>
                    <div class="prato-preco">R$ 23,00</div>
                </div>

                <div class="card">
                    <div class="prato-nome">Creme Brûlée</div>
                    <p class="prato-descricao">Creme de baunilha com crosta de açúcar queimado</p>
                    <div class="prato-preco">R$ 29,00</div>
                </div>
            </div>
        </div>

        <div class="footer">
            <p>© 2025 Byte Menu</p>
            <p>Telefone: (61) 9999-9999 | Brasília - DF</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    print("🚀 Byte Menu rodando: http://localhost:5000")
    app.run(debug=True, port=5000)