// Declaração de variáveis
// var, let, const
// var (escopo global ou local)
// let (escopo local)
// const (constante, valor não pode ser alterado)

let produto = 'Caneta';
let quantidade = 10;
let preco = 6.4;
let imposto = 1.5;
let precofinal = preco + imposto;

// Exibindo valores no console

console.log('Produto: ' + produto);
console.log('Quantidade: '+ quantidade + ' unidades');
console.log('Valor do produto: R$'+ preco);
console.log('Valor de imposto: R$'+ imposto);
console.log('Valor final: R$'+ precofinal);

// Alterando o valor da variável

produto = 'Caneta BIC';
console.log('Categoria: '+ produto);

/* Nomes de variáveis com mais de uma palavra
let nomeProduto = 'Caderno';
let nome_produto = 'Caderno';
let NomeProduto = 'Caderno';
*/