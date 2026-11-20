#!/usr/bin/node

function executeXtimes(x, theFunction) {
    for (let i = 0; i < x; i++) {
        theFunction();
    }
}

module.exports = executeXtimes;
