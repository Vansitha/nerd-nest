/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  if (s.length === 1) return true;

  const cleanStr = s.replace(/[^A-Za-z0-9]/g, "").toLowerCase();
  console.log(cleanStr);

  let start = 0;
  let end = cleanStr.length - 1;

  while (start < end) {
    if (cleanStr[start] === cleanStr[end]) {
      start++;
      end--;
    } else {
      return false;
    }
  }

  return true;
};

// const s = "A man, a plan, a canal: Panama";
// const s = "A man, a plan, a canal -- Panama";
const s = "Tracy, no panic in a pony-cart.";
// const s = "race a car";

const result = isPalindrome(s);
console.log(result);
