//imports: parte onde é importado objetos.
const visor = document.getElementById('display');
const buttons = document.querySelectorAll('button')



//função de clique: faz o trabalho do clique.
buttons.forEach(buttons  => {
    buttons.addEventListener('click', (evento) => {
        
        
        
        //funções basicas:
        if (evento.target.innerText === 'C') {
            visor.value = "";

        }
        else if (evento.target.innerText === '=' ){
            try{

                let check = visor.value.replaceAll('%', '/100')

            visor.value = Function('"use strict";return (' + check +')')();
        }
        catch (error) {
            visor.value = "Error";
            }
        } 
        else if (evento.target.innerText === '<'){
            visor.value =visor.value.slice(0, -1);
        }
        else {
            visor.value += evento.target.innerText;
            
        }
    });
});







//parte das observações:

//observação: pelo que eu aprendi para criar uma variavel é preciso usar const e
//escrever uma variavel

//quando for montar uma ram ou qualquer outra coisa que mude de valor use let

//visor.value = Function('"use strict";return (' + ram + ')')();

// variavel.value = variavel.value.slice(0, -1)