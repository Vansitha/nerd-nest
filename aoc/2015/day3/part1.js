const fs = require("fs");
const data = fs.readFileSync("input.txt", "utf8").trim().split("");

const directions = ['^','v','>','<'];

const seen = new Set();
let total = 0;
for (d of data) {
	if (seen.has(d)) continue;

}

console.log(total);
