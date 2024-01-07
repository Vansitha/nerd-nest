const fs = require("fs")
const data = fs.readFileSync("./input.txt", "utf8");

// Part 1
let floor = 0;

for(const c of data) {
	if (c === ")") floor--;
	if (c === "(") floor++;
}

console.log(floor);

// Part 2
floor = 0;
let position = 0;
const dataArr = data.split("");

for (let i = 0; i < dataArr.length; i++) {
	const c = dataArr[i];
	if (c === ")") floor--;
	if (c === "(") floor++;

	if (floor === -1) {
		position = i + 1;
		break;
	}
}

console.log(position);
