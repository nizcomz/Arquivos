// script.js

// Espera o documento HTML ser completamente carregado antes de manipular os elementos
document.addEventListener('DOMContentLoaded', function() {
    
    // 1. Obtém as referências dos elementos HTML pelos seus IDs
    const pageTitle = document.getElementById('pageTitle');
    const actionButton = document.getElementById('actionButton');
    const dynamicMessage = document.getElementById('dynamicMessage');
    
    let clickCount = 0; // Variável para controlar os cliques

    console.log("JavaScript carregado. Preparando a interatividade.");

    // 2. Adiciona o "ouvinte" de clique ao botão
    actionButton.addEventListener('click', function() {
        clickCount++;
        console.log(`Botão clicado ${clickCount} vezes!`);

        // 3. Lógica para mudar o conteúdo e o estilo
        if (clickCount === 1) {
            pageTitle.textContent = "Interagindo com JS!"; 
            dynamicMessage.textContent = "Você fez seu primeiro clique!";
            dynamicMessage.style.color = '#e65100'; // Muda a cor via JS
            actionButton.textContent = "Clique Mais!";
        } else if (clickCount === 2) {
            dynamicMessage.textContent = "Que legal, mais um clique!";
            dynamicMessage.style.color = '#2e7d32'; 
            pageTitle.style.color = '#c62828'; // Muda a cor do título via JS
        } else if (clickCount === 3) {
            dynamicMessage.textContent = "Três é um número mágico!";
            pageTitle.style.color = '#1a237e'; 
            actionButton.textContent = "Redefinir";
        } else {
            // Reseta tudo
            pageTitle.textContent = "Minha Página Mágica!";
            pageTitle.style.color = '#1a237e';
            dynamicMessage.textContent = "Mensagens aparecerão aqui...";
            dynamicMessage.style.color = '#00796b';
            actionButton.textContent = "Clique para Interagir!";
            clickCount = 0; 
        }
    });

    console.log("Interatividade pronta!");
});

