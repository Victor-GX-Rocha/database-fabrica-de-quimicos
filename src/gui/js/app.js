// js/app.js - Configuração principal da aplicação

class InventoryApp {
    constructor() {
        this.currentPage = 'dashboard';
        this.init();
    }

    init() {
        this.setupMenuEvents();
        this.loadPage('dashboard');
    }

    setupMenuEvents() {
        document.querySelectorAll(".menu-item").forEach(item => {
            item.addEventListener('click', (e) => {
                e.preventDefault();
                
                // Remove active de todos os itens
                document.querySelectorAll(".menu-item").forEach(i => {
                    i.classList.remove('active');
                });
                
                // Adiciona active ao item clicado
                item.classList.add("active");
                
                // Carrega a página correspondente
                const pageId = item.getAttribute('data-page');
                this.loadPage(pageId);
            });
        });
    }

    async loadPage(pageId) {
        try {
            this.showLoading();
            
            const response = await fetch(`src/gui/pages/${pageId}.html`);
            const html = await response.text();
            
            document.querySelector('.content').innerHTML = html;
            this.currentPage = pageId;
            
            // Inicializa scripts específicos da página
            this.initPageScripts(pageId);
            
        } catch (error) {
            console.error('Erro ao carregar página:', error);
            document.querySelector('.content').innerHTML = `
                <div class="page active">
                    <div class="page-header">
                        <h1>Erro</h1>
                        <p>Não foi possível carregar a página.</p>
                    </div>
                </div>
            `;
        }
    }

    initPageScripts(pageId) {
        // Carrega scripts específicos para cada página
        switch(pageId) {
            case 'register-product':
                if (typeof ProductForm !== 'undefined') {
                    new ProductForm();
                }
                break;
            case 'dashboard':
                // Inicializa dashboard se necessário
                break;
        }
    }

    showLoading() {
        document.querySelector('.content').innerHTML = `
            <div class="loading">
                <i class="fas fa-spinner fa-spin"></i>
                <p>Carregando...</p>
            </div>
        `;
    }
}

// Inicia a aplicação quando o DOM estiver carregado
document.addEventListener('DOMContentLoaded', () => {
    new InventoryApp();
});
