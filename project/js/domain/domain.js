"use strick"

class Product
{
    constructor(id, title, price){
        this._title = title;
        this._price = price
        this._id = id
    }

    // static getNextID()
    //     {
    //     Product.nextID += 1;
    //     return Product.nextID;
    // }

    get title(){
        return this._title;
    }

    get id(){
        return this._id;
    }

    get price() {
        return this._price;
    }
}
Product.nextID = 0;

class Domain
{
    static products(){
        let products = {};
        console.log(products.length);
        let Shaver = new Product("sh1", "Shaver", 9);
        let Gel = new Product("gsh1", "Shaver + Shaving gel", 13);
        let Aftershaves = new Product("agsh1", "Shaver + Shaving gel + Aftershaves", 23);
        products[Shaver.id] = Shaver;
        products[Gel.id] = Gel;
        products[Aftershaves.id] = Aftershaves;
        console.log(products.length);
        return products;
    }
}