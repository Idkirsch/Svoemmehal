// import dependencies 
//const https = require('https');

// create variable yWas and assign it no value
var yWas = null;


//create variable i and set it to 0
const i = 0;



const fetch = require("node-fetch");

fetch('https://l.vemcount.com/embed/data/W5mOsIMsECIwoYZ')
    .then(res => res.json())
    .then((out) => {
        console.log('Output: ', out);
}).catch(err => console.error(err));


//Næste skridt er at finde ud af hvordan man skriver værdierne fra et json objekt ud i html