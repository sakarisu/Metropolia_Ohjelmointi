'use strict';
const start = prompt('Which year do you want to start from? ')
const last = prompt('And what year will be the last? ')
let years = document.getElementById('years');
for(let i=start; i<=last; i++) {
    if ((0 == i % 4) && (0 != i % 100) || (0 == i % 400)) {
        let node = document.createElement('li')
        years.appendChild(node)
        node.innerHTML = i
    }
}
