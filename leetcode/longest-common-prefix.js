/**
 * @param {string[]} strs
 * @return {string}
 */
function longestCommonPrefix(strs) {
  if (strs.length === 0) return "";

  strs.sort();
  let result = new String();

  const firstStr = strs[0];
  const lastStr = strs[strs.length - 1];

  for (let i in firstStr) {
    if (firstStr[i] !== lastStr[i]) {
      break;
    }
    result += firstStr[i];
  }

  return result;
}

const strs = ["flower", "flow", "flight"];

const r = longestCommonPrefix(strs);
console.log(r);
