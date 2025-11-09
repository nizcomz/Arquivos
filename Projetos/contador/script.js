// Inicializar o contador com 0 
let cliques = 0;

// Selecione os elementos do DOM

const botao = document.getElementById('meuBotao');
const contador = document.getElementById('contador');

// Função que será chamado quando o botão for clicado 

if (botao && contador) {
    botao.addEventListener('click', function() {
        cliques++; // incrementa o contador
        contador.textContent = cliques; // Atualiza o texto
    });
} else {
    console.warn('Elemento(s) #meuBotao ou #contador não encontrado(s) no DOM.');
}
