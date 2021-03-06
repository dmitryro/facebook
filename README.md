# Facebook Questions

### 1. Longest Palindromic Substring
   
   **LeetCode No: 5**
   
   Given a string `s`, return longest palintromic substring in `s`.

### 2. Subarray Sum Equals K
   
   **LeetCode No: 560**

   Given an array of integers `nums` and integer `k`, return *the total number of
   continuous subarrays whos sum equals to `k`.

### 3. Random Pick with Weight

   **LeetCode No: 528**

   You are given an array of positive integers w where w[i] describes the weight of ith index (0-indexed).

We need to call the function pickIndex() which randomly returns an integer in the range [0, w.length - 1]. pickIndex() should return the integer proportional to its weight in the w array. For example, for w = [1, 3], the probability of picking the index 0 is 1 / (1 + 3) = 0.25 (i.e 25%) while the probability of picking the index 1 is 3 / (1 + 3) = 0.75 (i.e 75%).

More formally, the probability of picking index i is w[i] / sum(w).


### 4. Restore IP Addresses

**LeetCode No: 93**
    
   Given a string s containing only digits, return all possible valid IP addresses that can be obtained from s. You can return them in any order.

A valid IP address consists of exactly four integers, each integer is between 0 and 255, separated by single dots and cannot have leading zeros. For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses and "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.


### 5. Maximum Swap

**LeetCode No: 670**

Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.


### 6. Accounts Merge

**LeetCode No: 721**

Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are **emails** representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails **in sorted order**. The accounts themselves can be returned in **any order**. 


### 7. Best Time to Buy and Sell Stock
**LeetCode No: 121**

You are given an array prices where **prices[i]** is the **price** of a given stock on the **ith** day.

You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return `0`.


### 8. Copy List with Random Pointer

**LeetCode No: 138**
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a **deep copy** of the list. The **deep copy** should consist of exactly `n` **brand new** nodes, where each new node has its value set to the value of its corresponding original node. Both the `next` and `random` pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. **None of the pointers in the new list should point to nodes in the original list.**

For example, if there are two nodes `X` and `Y` in the original list, where `X.random --> Y`, then for the corresponding two nodes `x` and `y` in the copied list, `x.random --> y`.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of `[val, random_index]` where:

* `val`: an integer representing Node.val
* `random_index`: the index of the node (range from `0` to `n-1`) that the `random` pointer points to, or `null` if it does not point to any node.
Your code will **only** be given the `head` of the original linked list.


### 9. Word Break II
**LeetCode No: 140**

Given a string `s` and a dictionary of strings `wordDict`, add spaces in `s` to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in **any order**.

**Note** that the same word in the dictionary may be reused multiple times in the segmentation.

**Example 1:**
```
Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
```


**Example 2:**
```
Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.
```

**Example 3:**
```
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []
```


**Constraints:**
* **1 <= s.length <= 20**
* **1 <= wordDict.length <= 1000**
* **1 <= wordDict[i].length <= 10**
* **s and wordDict[i] consist of only lowercase English letters.**
* **All the strings of wordDict are unique.**


### 10. Binary Tree Right Side View

**LeetCode No: 199**

Given the `root` of a binary tree, imagine yourself standing on the **right side** of it, return *the values of the nodes you can see ordered from top to bottom*.

**Example 1**

```
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
```

**Example 2**

```
Input: root = [1,null,3]
Output: [1,3]
```

**Example 3**
```
Input: root = []
Output: []
```

**Constraints**
* **The number of nodes in the tree is in the range [0, 100].**
* **-100 <= Node.val <= 100**


### 11. Pow(x, n)

**LeetCode No: 50**

Implement pow(x, n), which calculates `x` raised to the power `n` (i.e., `x^n`).

 

**Example 1**

```
Input: x = 2.00000, n = 10
Output: 1024.00000
```

**Example 2**

```
Input: x = 2.10000, n = 3
Output: 9.26100
```

**Example 3**

```
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
```

**Constraints**

```
-100.0 < x < 100.0
-231 <= n <= 231-1
-104 <= xn <= 104
```

### 12. Generate Parentheses

**LeetCode No: 22**

Given `n` pairs of parentheses, write a function to *generate all combinations of well-formed parentheses*.


**Example 1**

```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
```

**Example 2**
```
Input: n = 1
Output: ["()"]
```

**Constraints**

* `1 <= n <= 8`

### 13. Combination Sum

**LeetCode No: 39**

Given an array of **distinct** integers `candidates` and a target integer `target`, return a *list of all* **unique combinations** of `candidates` *where the chosen numbers sum to* `target`. You may return the combinations in **any order**.

The **same** number may be chosen from candidates an **unlimited number of times**. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is **guaranteed** that the number of unique combinations that sum up to target *is less than* `150` combinations for the given input.

**Constraints**

* **1 <= candidates.length <= 30**
* **1 <= candidates[i] <= 200**
* **All elements of candidates are distinct.**
* **1 <= target <= 500**

**Example 1**
```
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
```


**Example 2**
```
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
```

**Example 3**
```
Input: candidates = [2], target = 1
Output: []
```

**Example 4**
```
Input: candidates = [1], target = 1
Output: [[1]]
```

**Example 5**
```
Input: candidates = [1], target = 2
Output: [[1,1]]
```


### 14. Product of Array Except Self
**LeetCode No: 238**

Given an integer array `nums`, return an array `answer` such that `answer[i]` *is equal to the product of all the elements of* `nums` *except* `nums[i]`.

The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

**Example 1**
```
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
```

**Example 2**
```
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

**Constraints**

* `2 <= nums.length <= 105`
* `-30 <= nums[i] <= 30`
* The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

**Follow up**

* Could you solve it in `O(n)` time complexity and without using division?
* Could you solve it with `O(1)` constant space complexity? (The output array **does not** count as extra space for space complexity analysis.)


### 15. Container With Most Water
**LeetCode No: 11**

Given `n` non-negative integers `a1, a2, ..., an` , where each represents a point at coordinate `(i, ai)`. `n` vertical lines are drawn such that the two endpoints of the line `i` is at `(i, ai)` and `(i, 0)`. Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.


**Notice** that you may not slant the container.


**Example 1**
```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
```

**Example 2**
```
Input: height = [1,1]
Output: 1
```

**Example 3**
```
Input: height = [4,3,2,1,4]
Output: 16
```

**Example 4**
```
Input: height = [1,2,1]
Output: 2
```

**Constraints**
```
n == height.length
2 <= n <= 105
0 <= height[i] <= 104
```




### 16. Number of Islands

**LeetCode No: 200**

Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return the number of islands.

An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

**Example 1**
```
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
```


**Example 2**
```
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

**Constraints**

* `m == grid.length`
* `n == grid[i].length`
* `1 <= m, n <= 300`
* `grid[i][j] is '0' or '1'`


### 17. Valid Word Abbreviation

**LeetCode No: 408**

Given a non-empty stringsand an abbreviationabbr, return whether the string matches with the given abbreviation.

A string such as"word"contains only the following valid abbreviations:

```["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]```

**Notice** that **only the above abbreviations** are valid abbreviations of the string"word". Any other string is not a valid abbreviation of"word".


**Note**
Assumescontains only lowercase letters andabbrcontains only lowercase letters and digits.

**Example 1**
```
Given 
s = "internationalization", 
abbr = "i12iz4n":

Return true.
```

**Example 2**
```
Given 
s = "apple", 
abbr = "a2e":

Return false.
```

