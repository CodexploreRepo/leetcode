# Sliding Windows

```C
nums = [100, 200, 100, 400, 500, 2, 600]
k = 3


// BRUTE FORCE O(N^2): iterate through all windows of size k
s1 = 100 + 200 + 100
s2 = 200 + 100 + 400
s3 = 100 + 400 + 500

for(int i = 0; i < n-k+1; i++){
    int current_sum = 0;

    for(int j = 0; j < k; j++){
        current_sum = current_sum + arr[i+j];
    }
    max_sum = max(current_sum, max_sum);    // pick maximum sum
}
```

<p align="center"><img src="../assets/img/sliding_windows_ex1.webp"></p>

```C
// SLIDING WINDOWS O(N):
int max_sum = 0, window_sum = 0;
/* calculate sum of 1st window */
for (int i = 0; i < k; i++)  window_sum += arr[i];
/* slide window from start to end in array. */

for (int i = k; i < n; i++){
    window_sum += arr[i] - arr[i-k];    // saving re-computation
    max_sum = max(max_sum, window_sum);
}
```

## Resources

- [Medium - Sliding Windows for Strings](https://medium.com/leetcode-patterns/leetcode-pattern-2-sliding-windows-for-strings-e19af105316b)
- [Leetcode - Sliding Window algorithm template to solve all the Leetcode substring search problem.](https://leetcode.com/problems/find-all-anagrams-in-a-string/solutions/92007/sliding-window-algorithm-template-to-solve-all-the-leetcode-substring-search-problem/)
- [Leetcode - C++ Maximum Sliding Window Cheatsheet Template](https://leetcode.com/problems/frequency-of-the-most-frequent-element/solutions/1175088/C++-Maximum-Sliding-Window-Cheatsheet-Template/)
