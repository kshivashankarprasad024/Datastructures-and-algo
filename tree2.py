class tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def printPreOrder(root):
    if root == None:
        return
 
    # root, left_subtree, right_subtree 
    print(root.data, end = " ")
    printPreOrder(root.left)
    printPreOrder(root.right)



root=tree(11)
obj1=tree(7)
obj2=tree(5)
obj3=tree(9)
obj4=tree(3)
obj5=tree(8)
obj6=tree(10)
obj7=tree(15)
obj8=tree(13)
obj9=tree(20)
obj10=tree(12)
obj11=tree(14)
obj12=tree(18)
obj13=tree(25)



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

printPreOrder(root)
