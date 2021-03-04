class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        
        for (int i = 0; i < nums.length; i++){
            map.put(target - nums[i], i);
        }
        for (int j = 0; j < nums.length; j++){
            if(map.containsKey(nums[j]) && map.get(nums[j]) != j ){
                return new int[] {j, map.get(nums[j])};
            }
        }
        throw new IllegalArgumentException("No two sum solution");
    }
    
}
