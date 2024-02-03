/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  if (nums.length < 2) return [];

  const diffMap = new Map();

  for (let i = 0; i < nums.length; i++) {
    const diff = target - nums[i]; // 9 - 2 = 7

    if (diffMap.has(diff)) {
      return [i, diffMap.get(diff)];
    }

    diffMap.set(nums[i], i);
  }
  return [];
};

const nums = [2, 7, 11, 15];
const target = 9;

const r = twoSum(nums, target);
console.log(r);
