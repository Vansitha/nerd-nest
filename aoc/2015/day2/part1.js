const fs = require("fs");
const data = fs.readFileSync("input.txt", "utf8").trim().split("\n");

let total = 0;
for (dimension of data) {
	const [ l,w,h ] = dimension.split("x");

	const a1 = l*w;
	const a2 = w*h;
	const a3 = h*l;

	const a = [a1,a2,a3];

	const minSide = Math.min(...a);
	const areaSum = a.reduce((acc, currVal) => acc + 2 * currVal, 0);

	total += minSide + areaSum;
}

console.log(total);
