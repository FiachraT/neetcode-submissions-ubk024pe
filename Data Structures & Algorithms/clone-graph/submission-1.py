"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #hashmap, node to node copy
        # for loop through neighbours, dfs
        newToOld = {}

        def dfs(node):
            # base case
            if node in newToOld:
                return newToOld[node]
            copy = Node(node.val)
            newToOld[node] = copy
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            return copy
        
        return dfs(node) if node else None



        