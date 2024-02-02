/**
 * @param {string} s
 * @return {number}
 */
var countGoodSubstrings = function (s) {
  if (s.length < 3) return 0;

  let count = 0;

  for (let i = 0; i < s.length - 2; i++) {
    const sw = new Set(s.slice(i, i + 3));
    if (sw.size === 3) {
      count++;
    }
  }

  return count;
};

const s = "xyzzaz";
console.log(countGoodSubstrings(s));
