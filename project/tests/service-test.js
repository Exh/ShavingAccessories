"use strick"

var assert = require('chai').assert;
var Subscribing = require('../js/domain/subscribing');
var User = require('../js/domain/user');
var Product = require('../js/domain/product');
var Domain = require('../js/domain/domain');

suite('Shaving accessories subscribing', function () {
    suite('As User I can', function () {

        test('to choose shaver as the product of subscribe', function () {
            let user = new User();
            let product = Domain.createShaver();
            let subscribing = new Subscribing(product);

            user.setSubscribing(subscribing);

            let res = user.subscribing.product.title;
            assert.equal(res, "Shaver")
        });

        test('to choose shaver + shaving gel as the product of subscribe', function () {
            let user = new User();
            let product = Domain.createShaverWithGel();
            let subscribing = new Subscribing(product);

            user.setSubscribing(subscribing);

            let res = user.subscribing.product.title;
            assert.equal(res, "Shaver + Shaving gel")
        });

        test('to choose shaver + shaving gel + aftershaves as the product of subscribe', function () {
            let user = new User();
            let product = Domain.createShaverWithGelWithAftershaves();
            let subscribing = new Subscribing(product);

            user.setSubscribing(subscribing);

            let res = user.subscribing.product.title;
            assert.equal(res, "Shaver + Shaving gel + Aftershaves")
        });

    });
});