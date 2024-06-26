class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 
 
 
def printPreOrder(root):
    if root == None:
        return
 
    # root, left_subtree, right_subtree 
    print(root.data)
    printPreOrder(root.left)
    printPreOrder(root.right)
 
def printInOrder(root):
    if root == None:
        return
 
    # left_subtree, root, right_subtree 
 
    printInOrder(root.left)
    print(root.data)
    printInOrder(root.right) 
 
def printPostOrder(root):
    if root == None:
        return
 
    # left_subtree, right_subtree, root
 
    printPostOrder(root.left)
    printPostOrder(root.right) 
    print(root.data)
 
 
def printLevelOrder(root):
    result = []
    Q = [root]
 
    while len(Q) > 0:
        n = len(Q)
        subResult = []
        for i in range(n):
            # step-1: popping
            curr = Q.pop(0)
            subResult.append(curr.data)
            
 
            # step-2: pushing left child if its not none 
            if curr.left != None:
                Q.append(curr.left)
                
                
 
            # step-3: pushing right child if its not none
            if curr.right != None:
                Q.append(curr.right)
                
 
        result.append(subResult)
        
 
    for subLevel in result:
        print(*subLevel)
    
root=TreeNode(11)
obj1=TreeNode(7)
obj2=TreeNode(5)
obj3=TreeNode(9)
obj4=TreeNode(3)
obj5=TreeNode(8)
obj6=TreeNode(10)
obj7=TreeNode(15)
obj8=TreeNode(13)
obj9=TreeNode(20)
obj10=TreeNode(12)
obj11=TreeNode(14)
obj12=TreeNode(18)
obj13=TreeNode(25)



root.left=obj1
root.right=obj7
obj1.left=obj2
obj1.right=obj3
obj2.left=obj4
obj3.left=obj5
obj3.right=obj6
obj7.left=obj8
obj7.right=obj9
obj8.left=obj10
obj8.right=obj11
obj9.left=obj12
obj9.right=obj13


printLevelOrder(root)
