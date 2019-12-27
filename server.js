console.log("Server side Hello World");

const express = require('express');
const server = express();

server.get("/json", (req, res) =>{
	res.json({message:"Client side Hello World"});
});

server.get("/", (req, res) => {
   res.sendFile(__dirname + '/index.html');
});

const port = 4000;

server.listen(port, () => {
    console.log(`Server listening at ${port}`);
});

server.get("/items", (req, res) => {
   res.json({ items: [{ "id": 1, "name": "banana" }, 
                      { "id": 2, "name": "apple" }
                     ] 
           });
});

server.get("/info", (req, res) => {
   res.sendFile(__dirname + '/info.html');
});

// let data = require('./data');


// server.get("/items", (req, res) => {
//    res.json(data);
// });


// server.get("/items/:id", (req, res) => {
//    const itemId = req.params.id;
//    const item = data.find(_item => _item.id === itemId);

//    if (item) {
//       res.json(item);
//    } else {
//       res.json({ message: `item ${itemId} doesn't exist`})
//    }
// });



