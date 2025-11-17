// ========== VARIÁVEIS GLOBAIS ==========
let contador = 0;
const temaSalvo = localStorage.getItem('tema') || 'claro';

// ========== INICIALIZAÇÃO ==========
document.addEventListener('DOMContentLoaded', function() {
    console.log('✅ Página carregada e pronta para interação');
    
    // Aplicar tema salvo
    if (temaSalvo === 'escuro') {
        document.body.classList.add('tema-escuro');
        document.getElementById('btnTema').textContent = '☀️ Tema Claro';
    }
    
    // Inicializar elementos
    inicializarContador();
    inicializarCalculadora();
    inicializarFormulario();
    inicializarTema();
    inicializarCores();
    atualizarInformacoes();
    
    // Atualizar informações a cada segundo
    setInterval(atualizarInformacoes, 1000);
});

// ========== CONTADOR ==========
function inicializarContador() {
    const btnIncrementar = document.getElementById('btnIncrementar');
    const btnDecrementar = document.getElementById('btnDecrementar');
    const btnResetar = document.getElementById('btnResetar');
    
    btnIncrementar.addEventListener('click', incrementarContador);
    btnDecrementar.addEventListener('click', decrementarContador);
    btnResetar.addEventListener('click', resetarContador);
}

function incrementarContador() {
    contador++;
    atualizarDisplay();
    console.log('Contador incrementado:', contador);
}

function decrementarContador() {
    contador--;
    atualizarDisplay();
    console.log('Contador decrementado:', contador);
}

function resetarContador() {
    contador = 0;
    atualizarDisplay();
    console.log('Contador resetado');
}

function atualizarDisplay() {
    document.getElementById('contador').textContent = contador;
    // Efeito visual
    document.getElementById('contador').style.animation = 'none';
    setTimeout(() => {
        document.getElementById('contador').style.animation = 'pulse 0.6s ease';
    }, 10);
}

// ========== CALCULADORA ==========
function inicializarCalculadora() {
    const btnCalcular = document.getElementById('btnCalcular');
    btnCalcular.addEventListener('click', realizarCalculo);
}

function realizarCalculo() {
    const num1 = parseFloat(document.getElementById('num1').value);
    const num2 = parseFloat(document.getElementById('num2').value);
    const operacao = document.getElementById('operacao').value;
    
    // Validação
    if (isNaN(num1) || isNaN(num2)) {
        exibirResultado('❌ Digite números válidos!', 'erro');
        return;
    }
    
    // Enviar para servidor Flask via AJAX
    fetch('/api/calcular', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            numero1: num1,
            numero2: num2,
            operacao: operacao
        })
    })
    .then(response => response.json())
    .then(data => {
        const resultado = data.resultado;
        const simbolos = {
            'soma': '+',
            'subtracao': '-',
            'multiplicacao': '×',
            'divisao': '÷'
        };
        const mensagem = `${num1} ${simbolos[operacao]} ${num2} = <strong>${resultado}</strong>`;
        exibirResultado(mensagem, 'sucesso');
        console.log('Cálculo realizado:', data);
    })
    .catch(erro => {
        console.error('Erro:', erro);
        exibirResultado('❌ Erro ao processar cálculo', 'erro');
    });
}

function exibirResultado(mensagem, tipo) {
    const elemento = document.getElementById('resultadoCalc');
    elemento.innerHTML = mensagem;
    elemento.className = 'resultado ativo ' + tipo;
}

// ========== FORMULÁRIO ==========
function inicializarFormulario() {
    const formulario = document.getElementById('formularioContato');
    formulario.addEventListener('submit', enviarFormulario);
}

function enviarFormulario(event) {
    event.preventDefault();
    
    const nome = document.getElementById('nome').value;
    const email = document.getElementById('email').value;
    const mensagem = document.getElementById('mensagem').value;
    
    // Validação
    if (!nome || !email || !mensagem) {
        exibirRespostaFormulario('❌ Todos os campos são obrigatórios!', 'erro');
        return;
    }
    
    // Enviar para servidor Flask via AJAX
    fetch('/api/processar-formulario', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            nome: nome,
            email: email,
            mensagem: mensagem
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.sucesso) {
            exibirRespostaFormulario(
                `✅ ${data.mensagem}<br><small>Enviado às ${data.timestamp}</small>`,
                'sucesso'
            );
            // Limpar formulário
            document.getElementById('formularioContato').reset();
            console.log('Formulário enviado:', data.dados_recebidos);
        } else {
            exibirRespostaFormulario('❌ Erro ao enviar formulário', 'erro');
        }
    })
    .catch(erro => {
        console.error('Erro:', erro);
        exibirRespostaFormulario('❌ Erro ao conectar com o servidor', 'erro');
    });
}

function exibirRespostaFormulario(mensagem, tipo) {
    const elemento = document.getElementById('mensagemResposta');
    elemento.innerHTML = mensagem;
    elemento.className = 'resposta ' + tipo;
    
    // Auto-esconder após 5 segundos
    if (tipo === 'sucesso') {
        setTimeout(() => {
            elemento.className = '';
        }, 5000);
    }
}

// ========== TEMA (Claro/Escuro) ==========
function inicializarTema() {
    const btnTema = document.getElementById('btnTema');
    btnTema.addEventListener('click', alternarTema);
}

function alternarTema() {
    const body = document.body;
    const btnTema = document.getElementById('btnTema');
    const temaAtivo = document.getElementById('temaAtivo');
    
    if (body.classList.contains('tema-escuro')) {
        // Mudar para claro
        body.classList.remove('tema-escuro');
        btnTema.textContent = '🌙 Tema Escuro';
        localStorage.setItem('tema', 'claro');
        temaAtivo.textContent = 'Claro';
        console.log('Tema alterado para: CLARO');
    } else {
        // Mudar para escuro
        body.classList.add('tema-escuro');
        btnTema.textContent = '☀️ Tema Claro';
        localStorage.setItem('tema', 'escuro');
        temaAtivo.textContent = 'Escuro';
        console.log('Tema alterado para: ESCURO');
    }
}

// ========== CORES INTERATIVAS ==========
function inicializarCores() {
    const btnMudarCor = document.getElementById('btnMudarCor');
    const btnCorAleatoria = document.getElementById('btnCorAleatoria');
    const corFundo = document.getElementById('corFundo');
    
    btnMudarCor.addEventListener('click', mudarCorFundo);
    btnCorAleatoria.addEventListener('click', gerarCorAleatoria);
    corFundo.addEventListener('change', mudarCorFundo);
}

function mudarCorFundo() {
    const cor = document.getElementById('corFundo').value;
    document.querySelector('.secao:nth-of-type(5)').style.backgroundColor = cor;
    console.log('Cor mudada para:', cor);
}

function gerarCorAleatoria() {
    const cores = [
        '#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8',
        '#F7DC6F', '#BB8FCE', '#85C1E2', '#F8B88B', '#D7BDE2'
    ];
    const corAleatoria = cores[Math.floor(Math.random() * cores.length)];
    document.getElementById('corFundo').value = corAleatoria;
    mudarCorFundo();
    console.log('Cor aleatória gerada:', corAleatoria);
}

// ========== INFORMAÇÕES DINÂMICAS ==========
function atualizarInformacoes() {
    // Atualizar hora
    const agora = new Date();
    const hora = agora.toLocaleTimeString('pt-BR');
    const data = agora.toLocaleDateString('pt-BR');
    
    document.getElementById('horaAtual').textContent = hora;
    document.getElementById('dataAtual').textContent = data;
    
    // User Agent (apenas uma vez)
    if (document.getElementById('userAgent').textContent === 'Carregando...') {
        const userAgent = navigator.userAgent.split(' ').slice(0, 3).join(' ');
        document.getElementById('userAgent').textContent = userAgent;
    }
}

// ========== UTILITÁRIOS ==========
// Log de ações no console
window.addEventListener('load', function() {
    console.log('%c🎨 Bem-vindo ao seu site interativo!', 'color: #3d5a80; font-size: 16px; font-weight: bold;');
    console.log('%cTemas de interação ativados:', 'color: #98c1d9; font-size: 12px;');
    console.log('✅ Contador interativo');
    console.log('✅ Calculadora AJAX');
    console.log('✅ Formulário dinâmico');
    console.log('✅ Alternador de tema');
    console.log('✅ Mudador de cores');
    console.log('✅ Informações em tempo real');
});