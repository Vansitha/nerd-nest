const fs = require("fs");
const data = fs.readFileSync("input.txt", "utf8").trim().split("\n");

let total = 0;
for (dimension of data) {
	const a = dimension.split("x").map(str => Number(str));
	const [s1, s2, s3] = a.slice().sort((a,b) => a - b);

	const p = s1*2+s2*2;
	const b = s1*s2*s3;

	total += p + b;

}

console.log(total);
