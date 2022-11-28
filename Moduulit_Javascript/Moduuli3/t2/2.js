'use strict'
const element = document.getElementById('target')
const list = ['First', 'Second', 'Third']
for(const i of list){
    const node = document.createElement('LI')
    element.appendChild(node)
    node.innerHTML = `${i} item`
}
element.className = 'my-item'