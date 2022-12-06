'use strict';
const lomake = document.querySelector('form');
const apiUrl = lomake.action;
const dialog = document.querySelector('dialog');
const closeDialog = document.querySelector('span');

async function fetchJson(url, options = {}) {
    const vastaus = await fetch(url, options);
    if (!vastaus.ok) {
        throw new Error(vastaus.statusText);
    }
    return await vastaus.json();
}

function createArticle(obj) {

    const article = document.createElement('article');
    const figure = document.createElement('figure');
    const img = document.createElement('img');
    const figcapt = document.createElement('figcapt');
    const url = document.createElement('a');
    const iframe = document.createElement('iframe')
    article.classname = 'card';
    article.innerHTML = `<h2>${obj.name}</h2>`;
    article.appendChild(figure);
    figure.appendChild(img);
    figure.appendChild(figcapt)
    figcapt.innerHTML = obj.genres.length?obj.genres.join(' | '):'Genreä ei löydy'
    img.src = obj.image!=null?obj.image.medium:"./errimg/error.png"
    article.innerHTML += `<p>${obj.summary}</p>`;
    url.innerHTML = 'Details;'
    url.target = 'blank_';
    article.appendChild(url);
    url.addEventListener('click', e =>{
        iframe.title = obj.name!=null?`<h2>${obj.name}</h2>`:'<h2><i>no name</i></h2>'
        iframe.src = obj.url
        iframe.width = 1000
        iframe.height = 700
        dialog.appendChild(iframe)
        dialog.showModal()
    })

    return article
}

lomake.addEventListener('submit', async function(evt) {
    try {
        evt.preventDefault();
        const hakusana = document.querySelector('#query').value;
        const sarjat = await fetchJson(apiUrl + '?q=' + hakusana);
        console.log(sarjat);
        const tiedot = sarjat.map(element => element.show)
        for(const i of tiedot) {
            document.getElementById('sarjat').appendChild(createArticle(i))
        }
    } catch (e) {
        console.error(e.message);
    }
})

closeDialog.addEventListener('click', e=>{
    dialog.close()
    dialog.removeChild(dialog.querySelector('iframe'))
})