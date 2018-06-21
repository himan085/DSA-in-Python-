# cook your dish here
#Tree class
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
#Height function
def height(root):
    if(root is None):
        return 0
        
    q = []
    q.append(root)
    h = 0
    
    while(1):
        nodeCount = len(q)
        if(nodeCount==0):
            return h
        h+=1
        while(nodeCount>0):
            a = q[0]
            q.pop(0)
            if(a.left is not None):
                q.append(a.left)
            if(a.right is not None):
                q.append(a.right)
            
            nodeCount-=1
        
        
#MAin methhod
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
print height(root)
