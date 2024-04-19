class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 
        self.prev = None 
 
def printLeftToRightManner(head):
    print("Left to Right")
    curr = head 
    while curr != None:
        print(curr.data, end = " --> ")
        curr = curr.next 
    print()
 
def printRightToLeftManner(head):
    print("Right to Left")
    tail = head 
    while tail.next != None:
        tail = tail.next 
 
    curr = tail
    while curr != None:
        print(curr.data, end = " --> ")
        curr = curr.prev 
    print()

def addNodeAtHeadOfLinkedList(head, val):
    newBlock = Node(val)
    if head == None:
        return newBlock
    newBlock.next = head 
    head.prev = newBlock 
    return newBlock
 
def deleteNodeAtSpecificPosition(head, position):
    if position == 1:
        return deleteHeadNodeInDoublyLinkedList(head)
    
    curr = head 
    index = 1 
 
    while index != position - 1:
        curr = curr.next 
        index += 1 
 
    nodeToBeDeleted = curr.next 
    nextNode = nodeToBeDeleted.next 
    curr.next = nextNode 
    nextNode.prev = curr 
    return head
 
l = [11, 22, 33, 44, 55, 66, 77]
head = None 
for val in l:
    head = addNodeAtHeadOfLinkedList(head, val)
printLeftToRightManner(head)
printRightToLeftManner(head)   
head=deleteNodeAtSpecificPosition(head, 2)
printLeftToRightManner(head)
printRightToLeftManner(head)   

