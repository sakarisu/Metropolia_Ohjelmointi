'use strict';
let dogs = [];
for(let i = 0; i < 6; i++) {
    dogs.push(prompt('What is the dogs name?'))
}
document.getElementById('dogs').innerHTML = '<ul><li>' + dogs.sort().reverse().join('</li><li>') + '</li></ul>'