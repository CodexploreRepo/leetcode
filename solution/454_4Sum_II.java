class Solution {
    public int fourSumCount(int[] A, int[] B, int[] C, int[] D) {
        int result = 0;
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        
        //Step 1: Take the arrays A and B, and compute all the possible sums of two elements
        for (int a: A) {
            for (int b: B){
                int sum = a + b;
                //Put the sum in the Hash map
                if (map.containsKey(sum)){
                    //increase the hash map value if more than 1 pair sums to the same value
                    map.put(sum, map.get(sum) + 1);
                } else{
                    map.put(sum, 1);
                }
            }
        }
        
        for (int c: C) {
            for (int d: D){
                //a + b + c + d = 0 => a + b = - (c + d)
                int sum = -(c + d);
                if (map.containsKey(sum)){
                    result+= map.get(sum);
                }
            }
        }
        
        return result;
    }
}
