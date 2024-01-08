public class BinarySearch {

  public static void main(String[] args) {

    int[] nums = { 1,2,3,4,5,6,7,8,9,10 }; 
    int target = 10;

    int result = binarySearch(nums, target);
    System.out.format("Index: %d value at index: %d\n", result, nums[result]);

  }

  private static int binarySearch(int[] nums, int target) {
    if (nums.length == 0) return -1;

    int start = 0;
    int end = nums.length - 1;

    while(start <= end) {
      int mid = (start + end) / 2;

      if (target == nums[mid]) {
        return mid;

      } else if (target < nums[mid]) {
        end = mid - 1;

      } else {
        start = mid + 1;
      }
    }

    return -1;
  }

}
