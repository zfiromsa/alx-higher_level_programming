#!/usr/bin/node

const args = process.argv;
const first_no = Number(args[2]);
if (Number.isNaN(first_no))
{
    console.log("Not a numbe");
}
else
{
    console.log("My number: ${first_no}");
}

