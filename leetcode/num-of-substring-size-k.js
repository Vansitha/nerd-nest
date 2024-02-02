/**
 * @param {number[]} arr
 * @param {number} k
 * @param {number} threshold
 * @return {number}
 */
var numOfSubarrays = function (arr, k, threshold) {
  if (arr.length < k) return 0;

  let count = 0;
  let partialTotal = 0;

  for (let i = 0; i < arr.length - k + 1; i++) {
    const winSize = arr.slice(i, i + k);

    if (partialTotal === 0) {
      const total = winSize.reduce((acc, value) => {
        return acc + value;
      }, 0);
      partialTotal = total;
    } else {
      partialTotal += winSize[winSize.length - 1];
    }

    const avg = partialTotal / k;

    if (avg >= threshold) {
      count++;
    }

    partialTotal -= winSize[0];
  }

  return count;
};

const arr = [2, 2, 2, 2, 5, 5, 5, 8];
const k = 3;
const threshold = 4;

const r = numOfSubarrays(arr, k, threshold);
console.log(r);
