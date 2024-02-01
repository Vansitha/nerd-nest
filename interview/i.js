function selectionSort(nums) {
  if (nums.length == 0) return [];

  for (let i = 0; i < nums.length; i++) {
    let min = i;
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[min] > nums[j]) {
        min = j;
      }
    }

    let temp = nums[i];
    nums[i] = nums[min];
    nums[min] = temp;
  }
}

const nums = [5, 3, 67, 31, 10, 7];
selectionSort(nums);
console.log(nums);
