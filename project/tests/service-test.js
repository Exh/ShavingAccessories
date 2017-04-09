"use strick"

var assert = require('chai').assert;
var Subscribing = require('../js/subscribing');
var User = require('../js/user');
var Product = require('../js/product');

suite('Shaving accessories subscribing', function () {
    suite('As User I can', function () {

        test('to choose shaver as the product of subscribe', function () {
            let user = new User();
            let product = new Product();
            let subscribing = new Subscribing(product);

            user.setSubscribing(subscribing);

            let res = user.subscribing.product.title;
            assert.equal(res, "Shaver")
        });
    });
});