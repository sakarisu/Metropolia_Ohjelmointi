'use strict';
const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];
for(const i of students){
  const node = document.createElement('OPTION')
  document.getElementById('target').appendChild(node)
  node.innerHTML = i.name
  node.value = i.id
}