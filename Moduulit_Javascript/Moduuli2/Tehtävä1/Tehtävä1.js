'use strict';
let numbers = []
let reverseNumbers = []
for(let i = 0; i < 5; i++) {
    numbers.push(prompt('Type a number'))
}
for(let i = numbers.length - 1; i >= 0; i--) {
    reverseNumbers.push(numbers[i])
}
console.log('The numbers in reverse are: ' + reverseNumbers)