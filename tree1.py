class tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
root=tree(2)
obj1=tree(7)
obj2=tree(5)
obj3=tree(2)
obj4=tree(6)
obj5=tree(5)
obj6=tree(11)
obj7=tree(9)
obj8=tree(4)


root.left=obj1
root.right=obj2
obj1.left=obj3
obj1.right=obj4
obj4.left=obj5
obj4.right=obj6
obj2.right=obj7
obj7.left=obj8
