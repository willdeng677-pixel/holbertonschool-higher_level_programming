#!/usr/bin/node
const callMeMoby = require('./101-call_me_moby.js');

callMeMoby(5, function () {
    console.log('Where I am!');
});
