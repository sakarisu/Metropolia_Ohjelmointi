'user strict'
const element = document.getElementById('trigger')
const img = document.getElementById('target')
element.addEventListener('mouseover', a=>{
    img.src = 'img/picB.jpg'
})
element.addEventListener('mouseout', a=>{
    img.src = 'img/picA.jpg'
})