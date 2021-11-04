const prompt = require('prompt-sync')()

function main(){

var media = 0;
var lista = [94,89,130,130,153,158,169,182,132,168,182,149];
for (var i = 0;i < lista.length; i++) {
    media += lista[i];
5
}
media = media/lista.length;
var varianca = 0;
for (var i = 0;i < lista.length; i++) {
    varianca += (media - lista[i]) * (media - lista[i]);
}
varianca = varianca/lista.length;
Math.sqrt(varianca);
}
main()