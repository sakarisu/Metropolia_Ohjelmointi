'use strict';
const throws = prompt('How many dices do you want to throw?')
var sum = 0
for(let i=0; i<=throws; i++) {
    sum += Math.floor(Math.random()*6)+1
}
document.getElementById('sum').innerHTML = 'The sum of the thrown dices is ' + sum