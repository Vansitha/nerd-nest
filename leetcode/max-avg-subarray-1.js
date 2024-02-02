/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findMaxAverage = function (nums, k) {
  if (nums.length < k) return 0;

  let windowSum = nums.slice(0, k).reduce((acc, value) => acc + value, 0);
  let windowAvg = windowSum / k;
  let maxAvg = windowAvg;

  for (let i = 0; i <= nums.length - k; i++) {
    console.log(i);
    windowSum = windowSum - nums[i] + nums[i + k];
    windowAvg = windowSum / k;
    maxAvg = Math.max(maxAvg, windowAvg);
  }

  return maxAvg;
};

const nums = [1, 12, -5, -6, 50, 3];
const k = 4;

const result = findMaxAverage(nums, k);
console.log(result);
