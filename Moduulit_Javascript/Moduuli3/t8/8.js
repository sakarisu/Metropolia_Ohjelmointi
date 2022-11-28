'user strict'
const button = document.getElementById('start')
const result = document.getElementById('result')
button.addEventListener('click', a=>{
    const mode = document.getElementById('operation').value
    const nums = [+document.getElementById('num1').value,
            +document.getElementById('num2').value]
    switch(mode){
        case 'add':
            val = nums[0] + nums[1]
            break
        case 'sub':
            val = nums[0] - nums[1]
            break
        case 'multi':
            val = nums[0] * nums[1]
            break
        case 'div':
            val = nums[0] / nums[1]
    }
    result.innerHTML = val
})