#!/usr/bin/node

const args = process.argv;
const [,,firts_arg] = args;
console.log(firts_arg || "No argument");

