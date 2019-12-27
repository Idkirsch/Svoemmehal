// import dependencies 
const https = require('https');

// create variable yWas and assign it no value
var yWas = null;
console.log(yWas);

//create variable i and set it to 0
const i = 0;
console.log(i);


const fetch = require("node-fetch");

fetch('https://l.vemcount.com/embed/data/W5mOsIMsECIwoYZ')
    .then(res => res.json())
    .then((out) => {
        console.log('Output: ', out);
}).catch(err => console.error(err));



// begin while-loop and make it run when i is equal to 0
// while (i==0){




// create variable data and get json object from url

// create variable y and load json from data

// last step: print y value
// }
