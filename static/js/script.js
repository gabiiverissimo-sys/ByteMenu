document.addEventListener('DOMContentLoaded', function() {
    console.log('Byte Menu carregado!');
    
// Filtro de categorias  
const categoriaBtns = document.querySelectorAll('.categoria-btn');
const categorias = document.querySelectorAll('.categoria'); 

categoriaBtns.forEach(btn => {
    btn.addEventListener('click', function() {
        categoriaBtns.forEach(b => b.classList.remove('active'));
        this.classList.add('active');
        
        const categoriaSelecionada = this.getAttribute('data-categoria');
        
        categorias.forEach(container => {
            const tituloCategoria = container.querySelector('.categoria-titulo').textContent.trim();
            let categoriaNoTitulo = '';
            
            // mapear o título para o data-categoria
            if (tituloCategoria === 'Entradas') {
                categoriaNoTitulo = 'entradas';
            } else if (tituloCategoria === 'Pratos Principais') {
                categoriaNoTitulo = 'principais';
            } else if (tituloCategoria === 'Sobremesas') {
                categoriaNoTitulo = 'sobremesas';
            } else if (tituloCategoria === 'Bebidas') { 
                categoriaNoTitulo = 'bebidas';
            } else if (tituloCategoria === 'Bebidas Alcoólicas') { 
                categoriaNoTitulo = 'alcoolicos';
            }
            
            // Esconde/mostra o contêiner 
            if (categoriaSelecionada === 'todos') {
                container.style.display = 'block';
            } else if (categoriaSelecionada === categoriaNoTitulo) {
                container.style.display = 'block';
            } else {
                container.style.display = 'none';
            }
        });
        
        
        pratoCards.forEach(card => {
            if (categoriaSelecionada === 'todos' || card.getAttribute('data-categoria') === categoriaSelecionada) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });
    
    });
});

    // adicionar ao carrinho
    const botoesAdicionar = document.querySelectorAll('.btn-adicionar');
    botoesAdicionar.forEach(btn => {
        btn.addEventListener('click', function() {
            const prato = this.getAttribute('data-prato');
            const preco = this.getAttribute('data-preco');
            alert(` ${prato} adicionado ao pedido!\nValor: R$ ${preco}`);
        });
    });
    
    // Botão fazer pedido
    document.querySelector('.btn-pedido').addEventListener('click', function() {
        alert(' Redirecionando para o sistema de pedidos...');
    });
    
    // Botão WhatsApp
    document.querySelector('.btn-whatsapp').addEventListener('click', function() {
        alert('📱 Abrindo WhatsApp para pedidos...');
    });
    
    // Botão hero
    document.querySelector('.btn-hero').addEventListener('click', function() {
        document.getElementById('cardapio').scrollIntoView({
            behavior: 'smooth'
        });
    });
    
    // Smooth scroll para links de navegação
    document.querySelectorAll('nav a').forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            document.querySelector(targetId).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
});