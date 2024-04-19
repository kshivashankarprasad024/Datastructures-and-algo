class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
def PrintLeftToRight(head):
    print("left to right")
    curr=head
    while curr!=None:
        print(curr.data,end="-->")
        curr=curr.next
    print()
def PrintRightToLeft(tail):
    print("right to left")
    curr=tail
    while curr!=None:
        print(curr.data,end="-->")
        curr=curr.prev
    print()

obj1=node(40)
obj2=node(50)
obj3=node(60)
obj4=node(70)
obj5=node(80)
obj1.next=obj2
obj2.next=obj3
obj3.next=obj4
obj4.next=obj5
obj2.prev=obj1
obj3.prev=obj2
obj4.prev=obj3
obj5.prev=obj4
PrintLeftToRight(obj1)
PrintRightToLeft(obj5)
