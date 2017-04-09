"use strick"

class Product
{
    constructor(){
        this._title = "Shaver";
    }

    get title(){
        return this._title;
    }
}

module.exports = Product;