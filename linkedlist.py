class node:
    def __init__(self,data):
        self.data=data
        self.next=None
obj1=node(20)
obj2=node(30)
obj3=node(40)
obj4=node(50)
obj5=node(60)
obj6=node(70)
obj7=node(80)
obj8=node(90)
obj9=node(100)
obj10=node(110)
obj1.next=obj2
obj2.next=obj3
obj3.next=obj4
obj4.next=obj5
obj5.next=obj6
obj6.next=obj7
obj7.next=obj8
obj8.next=obj9
obj9.next=obj10
curr=obj1
while curr!=None:
    print(curr.data,end="-->")
    cur =curr.next
