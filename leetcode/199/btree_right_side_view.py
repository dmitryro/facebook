# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    
    Thought Process:
    
    Way1: BFS
        Put the last node in the same level order in to list
       1 
      / \
     2   3
     
     using bfs and put node in the same level into a list we can have
        ans = [[1],[2,3]]
    And we always get the last node in the same level 
        ans = [i[-1] for i in ans]
        
    Way2: DFS
        start from root node -> right subtree -> left subtree
        With this order, the fisr node we traversed in each detph(1, 2, 3...) is what we want
    """
    def rightSideView(self, root: TreeNode) -> List[int]:
        """
        T:O(n) since each node is only visited once but it has two passes
        S:O(h) if it's balanced tree
        """
        if not root:
            return []
        
        q = collections.deque([(root, 1)])
        ordered_from_top_to_bottom = []
        while len(q) != 0:
            cur_node, depth = q.popleft()
            if cur_node.left:
                q.append((cur_node.left, depth+1))
            if cur_node.right:
                q.append((cur_node.right, depth+1))
            
            while len(ordered_from_top_to_bottom) < depth:
                ordered_from_top_to_bottom.append([])
                
            ordered_from_top_to_bottom[depth-1].append(cur_node.val)
        
        return [ls_node_in_same_level[-1] for ls_node_in_same_level in ordered_from_top_to_bottom]
    
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        self.ordered_from_top_to_bottom = []
        def dfs(r, depth = 1):
            if r:
                if depth > len(self.ordered_from_top_to_bottom):
                    self.ordered_from_top_to_bottom.append(r.val)
                dfs(r.right, depth+1)
                dfs(r.left, depth+1)
        
        dfs(root, 1)
        
        return self.ordered_from_top_to_bottom
