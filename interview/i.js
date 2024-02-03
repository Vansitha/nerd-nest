const nums = [5, 6, 72, 7, 820, 10];
console.log(nums);

const nums2 = [...nums];
console.log(nums2);

nums2.length = 0;
console.log(nums);
console.log(nums2);
