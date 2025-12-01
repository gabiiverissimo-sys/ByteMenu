document.addEventListener('DOMContentLoaded', function() {

    const bars = document.querySelector('.bars');
    let menuCriado = false;
    let menuOverlay;

    // Recupera usuário logado do localStorage
    const usuarioLogado = JSON.parse(localStorage.getItem('usuario')); 
    // Estrutura esperada: { nome: "Gabriella", email: "...", token: "..." }

    bars.addEventListener('click', function() {
        if (!menuCriado) {
            criarMenuReserva();
            menuCriado = true;
        }
        toggleMenu();
    });

    function criarMenuReserva() {
        menuOverlay = document.createElement('div');
        menuOverlay.className = 'menu-overlay';
        menuOverlay.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.7);
            z-index: 1000;
            display: none;
        `;

        const menuLateral = document.createElement('div');
        menuLateral.className = 'menu-lateral';
        menuLateral.style.cssText = `
            position: fixed;
            top: 0;
            right: -300px;
            width: 280px;
            height: 100%;
            background: #3e2723;
            z-index: 1001;
            transition: right 0.3s ease;
            padding: 80px 20px 20px;
            box-shadow: -5px 0 15px rgba(0,0,0,0.3);
        `;

        // Monta o menu da página de reservas
        let menuHTML = `
            <nav style="display: block !important;">
                <ul style="list-style: none; padding: 0; margin: 0;">
                    <li style="margin-bottom: 20px; color: #c89b3c; font-size: 1.2rem; font-weight: bold; padding: 10px; border-bottom: 1px solid #c89b3c;">
                        👤 ${usuarioLogado ? usuarioLogado.nome : "Usuário"}
                    </li>
                    <li style="margin-bottom: 20px;">
                        <a href="/" style="color: #c89b3c; text-decoration: none; font-size: 1.2rem; font-weight: bold; display: block; padding: 10px; border-bottom: 1px solid #c89b3c;">
                            Início
                        </a>
                    </li>
                </ul>
            </nav>
            <button class="fechar-menu" style="position: absolute; top: 20px; right: 20px; background: none; border: none; color: #c89b3c; font-size: 1.5rem; cursor: pointer;">✕</button>
        `;

        menuLateral.innerHTML = menuHTML;

        document.body.appendChild(menuOverlay);
        document.body.appendChild(menuLateral);

        menuOverlay.addEventListener('click', toggleMenu);
        menuLateral.querySelector('.fechar-menu').addEventListener('click', toggleMenu);
    }

    function toggleMenu() {
        const menuLateral = document.querySelector('.menu-lateral');
        const menuOverlay = document.querySelector('.menu-overlay');
        
        if (menuLateral.style.right === '0px') {
            menuLateral.style.right = '-300px';
            menuOverlay.style.display = 'none';
        } else {
            menuLateral.style.right = '0px';
            menuOverlay.style.display = 'block';
        }
    }
});
