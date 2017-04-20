"use strick"



if (require) {
    console.log("Require product");

    var Product = require('./product');
}

class Domain
{
    static products(){
        let products = [];
        console.log(products.length);
        let Shaver = createShaver();
        let Gel = createShaverWithGel();
        let Aftershaves = createShaverWithGelWithAftershaves();
        products[Shaver.id] = Shaver;
        products[Gel.id] = Gel
        products[Aftershaves.id] = Aftershaves;
        console.log(product.length);
        return products;
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

if (typeof module != "undefined") {
    module.exports = Domain;
}