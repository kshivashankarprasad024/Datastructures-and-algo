class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
 
def printLinkedList(head):
    curr = head
    while curr != None:
        print(curr.data, end = " --> ")
        curr = curr.next
    print()
def insertNodeAtHeadOfLinkedList(head, ele):
    newBlock = Node(ele)
    if head == None:
        return newBlock
    newBlock.next = head 
    return newBlock
def DeleteHeadNode(head):
    if head==None:
        return None
    secondnode=head.next
    head.next=None
    return secondnode
def DeleteNodeAtSpecificPosition(head,position):
    if position==1:
        return DeleteHeadNode(head)
    curr=head
    index=1
    while index!=position-1:
        curr=curr.next
        index+=1
    mainnode=curr.next
    nextnode=mainnode.next
    mainnode.next=None
    curr.next=None
    curr.next=nextnode
    return head
l = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110]
head = None 
for ele in l:
    head = insertNodeAtHeadOfLinkedList(head, ele)
printLinkedList(head)
head=DeleteNodeAtSpecificPosition(head,4)
printLinkedList(head)
head=DeleteNodeAtSpecificPosition(head,1)
printLinkedList(head)




