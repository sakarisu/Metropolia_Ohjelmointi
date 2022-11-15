'use strict';
const start = confirm('Should I calculate the square root?')
let result

if (start){
    const number = prompt('Type in a number: ')
        let sqrt = Math.sqrt(number);
        result = 'The square root of ' + number + ' is ' + sqrt;
        if (number < 0) {
            result = 'The square root of a negative is not defined.'
        }
} else {
    result ='The square is not calculated'
}
document.getElementById('result').innerHTML = result