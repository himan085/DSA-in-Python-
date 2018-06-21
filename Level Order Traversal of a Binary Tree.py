# cook your dish here
#Tree class
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
#Height function
def bfs(root):
    if(root is None):
        return 
        
    q = []
    q.append(root)
    
    while(len(q) > 0):
    
        a = q[0]
        q.pop(0)
        print a.data,
        if(a.left is not None):
            q.append(a.left)
        if(a.right is not None):
            q.append(a.right)
        
        
#MAin methhod
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
bfs(root)
