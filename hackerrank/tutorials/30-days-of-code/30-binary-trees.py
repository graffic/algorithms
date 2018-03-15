import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root
    def levelOrder(self,root):
        result = []
        current_stack = [root]
        while len(current_stack) > 0:
            result.extend(n.data for n in current_stack)
            current_stack = [c for n in current_stack for c in (n.left, n.right) if c != None]
        print(" ".join(str(x) for x in result))
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
