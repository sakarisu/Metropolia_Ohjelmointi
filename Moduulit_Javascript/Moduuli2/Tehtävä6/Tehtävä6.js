'use strict';
function rollDice() {
    return Math.floor(Math.random()*6)+1;
}
const rolls = [];
var result = 0
do {
    result = rollDice()
    rolls.push(result)
}while(result < 6)
document.getElementById('rolls').innerHTML = '<ul><li>' + rolls.join('</li><li>') + '</li></ul>'