'use strict';

const map = L.map('map', {tap: false});
L.tileLayer('https://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
  maxZoom: 20,
  subdomains: ['mt0', 'mt1', 'mt2', 'mt3'],
}).addTo(map);
map.setView([60, 24], 7);

const apiUrl = 'http://127.0.0.1:3000/';

const tummaIcon = L.divIcon({className: 'tumma-icon'});
const vaaleaIcon = L.divIcon({className: 'vaalea-icon'});

async function getData(url) {
  const response = await fetch(url);
  if (!response.ok) throw new Error('Invalid server input!');
  const data = await response.json();
  console.log(data);
  return data;
}

function checkContinent() {
  const vastaus = 'http://127.0.0.1:3000/haeMaanosa/YSSY';  //testi-ICAO     //url+'haeMaanosa/OMSN
  const kaydyt = []
  if (vastaus === 'AS' && !kaydyt.includes('AS')) {
    document.getElementById('Aasia').classList.remove('hidden')
    kaydyt.append(vastaus)
  } else if (vastaus === 'AF' && !kaydyt.includes('AF')) {
    document.getElementById('Afrikka').classList.remove('hidden')
    kaydyt.append(vastaus)
  } else if (vastaus === 'PA' && !kaydyt.includes('PA')) {
    document.getElementById('P-amerikka').classList.remove('hidden')
    kaydyt.append(vastaus)
  } else if (vastaus === 'EA' && !kaydyt.includes('EA')) {
    document.getElementById('E-amerikka').classList.remove('hidden')
    kaydyt.append(vastaus)
  } else if (vastaus === 'EU' && !kaydyt.includes('EU')) {
    document.getElementById('Eurooppa').classList.remove('hidden')
    kaydyt.append(vastaus)
  } else if (vastaus === 'OC' && !kaydyt.includes('OC')) {
    document.getElementById('Oseania').classList.remove('hidden')
    kaydyt.append(vastaus)
  } else if (vastaus === 'AN' && !kaydyt.includes('AN')) {
    document.getElementById('Antarktika').classList.remove('hidden')
    kaydyt.append(vastaus)
  } else {
    alert('Error')
  }
}

async function pelinAloitus() {
  try {
    const nimi = prompt('Kirjoita nimesi');
    document.getElementById('pelaaja-nimi').innerHTML = nimi;
    const lentokentät = getData(apiUrl + 'haeLentokentat');
  } catch (error) {
    console.log(error);
  }
}

pelinAloitus();
checkContinent(apiUrl)
