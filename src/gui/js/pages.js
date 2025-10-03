// js/pages.js - Gerencia o carregamento de páginas
class PageManager {
    static async loadPage(pageId) {
        try {
            const response = await fetch(`src/gui/pages/${pageId}.html`);
            return await response.text();
        } catch (error) {
            return `<div class="error-page">
                <h2>Página não encontrada</h2>
                <p>A página ${pageId} não pôde ser carregada.</p>
            </div>`;
        }
    }
}
