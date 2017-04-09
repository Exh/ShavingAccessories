var Product = require('./js/product');

var express = require('express');
var bodyParser = require('body-parser');
var app = express();

var urlencodedParser = bodyParser.urlencoded({ extended: false })

app.use(express.static('public'));
app.get('/index.htm', function (req, res) {
    res.sendFile( __dirname + "/html/" + "index.htm" );
});

app.get('/', function (req, res) {
    let product = new Product();
    res.send(product.title);
})

app.get('/process_get', function (req, res) {
    // Prepare output in JSON format
    response = {
        first_name:req.query.first_name,
        last_name:req.query.last_name
    };
    res.end(JSON.stringify(response));
})

app.post('/process_post', urlencodedParser, function (req, res) {
    // Prepare output in JSON format
    response = {
        first_name:req.body.first_name,
        last_name:req.body.last_name
    };
    console.log(response);
    res.end(JSON.stringify(response));
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