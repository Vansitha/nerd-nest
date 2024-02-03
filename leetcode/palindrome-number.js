/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function (x) {
  if (x < 0) return false;

  const numStr = String(x);
  let start = 0;
  let end = numStr.length - 1;

  while (start < end) {
    if (numStr[start] !== numStr[end]) {
      return false;
    }
    start++;
    end--;
  }
  return true;
};

const x = -121;
const r = isPalindrome(x);

console.log(r);
