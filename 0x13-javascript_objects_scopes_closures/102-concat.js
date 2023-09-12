#!/usr/bin/node
const dg = require('fs');
const dFile = dg.readFileSync(process.argv[2]).toString();
const gFile = dg.readFileSync(process.argv[3]).toString();
dg.writeFileSync(process.argv[4], dFile + gFile);
