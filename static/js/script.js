document.addEventListener('DOMContentLoaded', function() {
    console.log('Byte Menu carregado!');
    
    // Filtro de categorias
    const categoriaBtns = document.querySelectorAll('.categoria-btn');
    const pratoCards = document.querySelectorAll('.prato-card');
    
    categoriaBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            // Remove active de todos os botões
            categoriaBtns.forEach(b => b.classList.remove('active'));
            // Adiciona active no botão clicado
            this.classList.add('active');
            
            const categoria = this.getAttribute('data-categoria');
            
            // filtra os pratos
            pratoCards.forEach(card => {
                if (categoria === 'todos' || card.getAttribute('data-categoria') === categoria) {
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