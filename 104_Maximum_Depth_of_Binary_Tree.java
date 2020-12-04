class Solution {
    public int maxDepth(TreeNode root) {
        //DFS: Depth First Search > Recursive Algo
        
        //Base Case:
        if (root == null){
            return 0;
        }
        //Recursive Case:
        int depthLeft = maxDepth(root.left);
        int depthRight = maxDepth(root.right);
        
        return Math.max(depthLeft, depthRight) + 1;
        
            
    }
}
