'use strict';
const names = ['John', 'Paul', 'Jones'];
for(let i of names){
    const node = document.createElement('LI')
    document.getElementById('target').appendChild(node)
    node.innerHTML = i
}