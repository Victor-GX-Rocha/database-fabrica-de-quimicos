// js/product-form.js - Lógica do formulário de produtos
class ProductForm {
    constructor() {
        this.container = document.getElementById('produtos-container');
        this.init();
    }

    init() {
        this.setupEventListeners();
        console.log('Formulário de produtos inicializado');
    }

    setupEventListeners() {
        // Usamos event delegation para lidar com elementos dinâmicos
        document.addEventListener('click', (e) => {
            if (e.target.classList.contains('btn-adicionar-produto')) {
                this.adicionarProduto();
            }
            if (e.target.classList.contains('btn-cadastrar-produto')) {
                this.cadastrarProduto(e.target);
            }
            if (e.target.classList.contains('btn-remover-produto')) {
                this.removerProduto(e.target);
            }
        });
    }

    adicionarProduto() {
        const template = document.getElementById('produto-template');
        const novoProduto = template.content.cloneNode(true);
        this.container.appendChild(novoProduto);
    }

    cadastrarProduto(button) {
        const bloco = button.closest('.produto-form');
        this.mostrarBotoesEdicao(bloco);
        
        // Aqui você pode adicionar validação do formulário
        this.validarFormulario(bloco);
    }

    removerProduto(button) {
        const bloco = button.closest('.produto-form');
        bloco.remove();
    }

    mostrarBotoesEdicao(bloco) {
        bloco.querySelector('.btn-cadastrar-produto').style.display = 'none';
        bloco.querySelector('.btn-editar-produto').style.display = 'inline-block';
        bloco.querySelector('.btn-remover-produto').style.display = 'inline-block';
    }

    validarFormulario(bloco) {
        const inputs = bloco.querySelectorAll('input[required], select[required]');
        let valido = true;

        inputs.forEach(input => {
            if (!input.value.trim()) {
                input.style.borderColor = 'var(--danger)';
                valido = false;
            } else {
                input.style.borderColor = '';
            }
        });

        return valido;
    }
}
