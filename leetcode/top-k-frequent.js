/**
  * @param {number[]} nums
  * @param {number} k
  * @return {number[]}
  */
function topKFrequent (nums, k) {
  const freqMap = new Map();

  for (let num of nums) {
    if (freqMap.has(num)) {
      freqMap.set(num, (freqMap.get(num) + 1));
      continue;
    }
    freqMap.set(num, 1);
    }

  const entries = Array.from(freqMap.entries());
  const sortedEntires = entries.sort((a,b) => b[1] - a[1]);

  let result = new Array();
  for (let i = 0; i < k; i++) {
    result.push(sortedEntires[i][0]);
  }

  return result;

}

const nums = [1];
const k = 1;

const result = topKFrequent(nums, k);
console.log(result);
