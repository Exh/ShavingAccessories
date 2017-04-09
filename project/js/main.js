var Product = require('../js/product');

var express = require('express');
var app = express();

app.get('/', function (req, res) {
    let product = new Product();
    res.send(product.title);
})

// This responds a POST request for the homepage
app.post('/', function (req, res) {
    console.log("Got a POST request for the homepage");
    res.send('Hello POST');
})


var server = app.listen(8081, function () {
    var host = server.address().address;
    var port = server.address().port;

    console.log("listening at http://%s:%s", host, port)
})