/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  if (numbers.length === 0) return [];

  let start = 0;
  let end = nums.length - 1;

  while (start < end) {
    const currTotal = nums[start] + nums[end];
    if (currTotal === target) {
      return [start, end];
    } else if (currTotal > target) {
      end -= 1;
    } else {
      start += 1;
    }
  }
  return [];
};

const numbers = [2, 7, 11, 15];
const target = 9;

const result = twoSum(numbers, target);
console.log(result);
