/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function (s) {
  const numMap = {
    I: 1,
    V: 5,
    X: 10,
    L: 50,
    C: 100,
    D: 500,
    M: 1000,
  };

  const charArr = Array.from(s.trim());

  let prev = 0;
  let count = 0;
  for (let char of charArr) {
    let num = numMap[char];
    if (prev < num && prev !== 0) {
      num = num - prev - prev;
    }
    prev = num;
    count += num;
  }

  return count;
};

const s = "LVIII";
console.log(s, romanToInt(s));
