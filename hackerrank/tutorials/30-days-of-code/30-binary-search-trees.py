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
    def getHeight(self,root):
        max_height = 0
        stack = [(0, root)]
        
        while len(stack) > 0:
            current_height, current_node = stack.pop()
            if current_node.left == current_node.right == None:
                max_height = max(max_height, current_height)
                continue
            for node in (current_node.left, current_node.right):
                stack.append([current_height + 1, node]) if node else None

        return max_height
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)       