'use strict';
let people = []
let count = prompt('How many participants are there?')
for(let i = 0; i < count; i++) {
    people.push(prompt('Type the participants name'))
}
document.getElementById('participants').innerHTML = '<ol><li>'+people.sort().join('</li><li>')+'</li></ol>'