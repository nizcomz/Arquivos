

//1° bloco de código
{ //Aqui temos as primeiras seis sentenças do bloco de código 
    console.log('Este primeiro bloco de código exibe números impares');
    console.log(1);
    console.log(3);
    console.log(5);
    console.log(7);
    console.log(9);
}



//2° bloco de código
{ //Aqui temos mais seis sentenças do bloco
    console.log('Esse segundo bloco de código exibe números pares');
    console.log(2);
    console.log(4);
    console.log(6);
    console.log(8);
    console.log(10);
}


console.log('Números ímpares:')
for (let i = 1; i <= 9; i += 2) console.log(i)

console.log('Números pares:')
for (let i = 2; i <= 10; i += 2) console.log(i)

/*
A estrutura de repetição "for" é utilizada para repetir um bloco de código um número específico de vezes,
neste caso, para exibir números ímpares e pares dentro de um intervalo definido.
*/