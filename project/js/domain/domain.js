"use strick"


var Product = require('./product');

class Domain
{
    static products(){
        let product = [];
        console.log(products.length);
        let Shaver = createShaver();
        let Gel = createShaverWithGel();
        let Aftershaves = createShaverWithGelWithAftershaves();
        product[Shaver.id] = Shaver;
        product[Gel.id] = Gel
        product[Aftershaves.id] = Aftershaves;
        console.log(products.length);
        return product;
    }

    static createShaver()
    {
        return new Product("sh1", "Shaver", 1);
    }
    static createShaverWithGel()
    {
        return new Product("gsh1", "Shaver + Shaving gel", 9);
    }

    static createShaverWithGelWithAftershaves()
    {
        return new Product("agsh1", "Shaver + Shaving gel + Aftershaves", 17);
    }
}

Domain.products = [];

module.exports = Domain;