'use strict'
const n1 = parseInt(prompt('Type a number: '))
const n2 = parseInt(prompt('Type the second number: '))
const n3 = parseInt(prompt('Type the last number: '))
const sum = n1+n2+n3
const pro = n1*n2*n3
const ave = sum/3
document.getElementById('ans').innerHTML = 'The sum of the given numbers is ' + sum + '<br> The product is ' + pro + '<br> And the average is ' + ave