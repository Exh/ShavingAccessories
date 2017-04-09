"use strick"

class User
{
    constructor(){

    }

    setSubscribing(subscribing) {
        this._subscribing = subscribing;
    }

    get subscribing() {
        return this._subscribing;
    }
}

module.exports = User;