'use strict';
let sides = parseInt(prompt('How many sides does the dice have?'));
function rollDice(sides) {
    return Math.floor(Math.random()*sides)+1;
}
const rolls = [];
var result = 0
do {
    result = rollDice(sides)
    rolls.push(result)
}while(result < sides)
document.getElementById('rolls').innerHTML = '<ul><li>' + rolls.join('</li><li>') + '</li></ul>'