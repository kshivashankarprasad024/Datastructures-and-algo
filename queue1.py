class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
 
def printLinkedList(head):
    curr = head
    while curr != None:
        print(curr.data, end = " ")
        curr = curr.next
    print()
def insertAtEndOfTail(head,ele):
    newblock=Node(ele)
    if head ==None:
        return newblock
    curr=head
    while curr.next != None:
        curr=curr.next
    curr.next=newblock
    return head
def DeleteHeadNode(head):
    if head==None:
        return None
    secondnode=head.next
    head.next=None
    return secondnode
n=int(input())
l=list(map(int,input().split()))
head = None 
for ele in l:
    head = insertAtEndOfTail(head, ele)
 
printLinkedList(head)
head=DeleteHeadNode(head)
printLinkedList(head)
