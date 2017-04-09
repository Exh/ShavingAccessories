"use strick"

class Subscribing
{
    constructor(product){
        this._product = product;
    }

    setProduct(product) {
        this._product = product;
    }

    get product(){
        return this._product;
    }
}

module.exports = Subscribing;