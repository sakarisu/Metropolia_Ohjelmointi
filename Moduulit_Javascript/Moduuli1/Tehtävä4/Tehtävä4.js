'use strict';
let house
const name = prompt('What is your name? ')
const sort = Math.floor(Math.random()*4)+1
if (sort == 1) {
    house = 'Gryffindor'
}
else if (sort == 2) {
    house = 'Hufflepuff'
}
else if (sort == 3) {
    house = 'Ravenclaw'
}
else if (sort == 4) {
    house = 'Slytherin'
}
document.getElementById('choice').innerHTML = name + ', you are a ' + house