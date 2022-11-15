'use strict';
let leap
function checker(year) {
    if ((0 == year % 4) && (0 != year % 100) || (0 == year % 400)) {
            leap =  (year + ' is a leap year.');
        } else {
            leap = (year + ' is not a leap year.');
    }
}
const year = prompt('Type in the year you want to check: ');
checker(year);
document.getElementById('leap').innerHTML = leap