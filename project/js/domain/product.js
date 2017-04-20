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

module.exports = Product;