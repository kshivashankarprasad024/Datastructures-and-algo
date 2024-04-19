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
l = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110]
head = None 
for ele in l:
    head = insertNodeAtHeadOfLinkedList(head, ele)
 
printLinkedList(head)
head=DeleteHeadNode(head)
printLinkedList(head)
