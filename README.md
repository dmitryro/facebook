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

** LeetCode No: 50**

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


