class node:
    def __init__(self,data):
        self.data=data
        self.next=None
def printlinkedlist(head):
    curr=head
    while curr != None:
        print(curr.data,end="-->")
        curr=curr.next
    print()
def insertAtEndOfTail(head,ele):
    newblock=node(ele)
    if head ==None:
        return newblock
    curr=head
    while curr.next != None:
        curr=curr.next
    curr.next=newblock
    return head
l=[11,22,56,78,98,90,34,56,79]
head=None
for ele in l:
    head=insertAtEndOfTail(head,ele)
printlinkedlist(head)   
    
