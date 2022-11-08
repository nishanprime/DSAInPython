class Node:
    def __init__(self,val):
        self.value=val
        self.next= None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    def add(self,value):
        newNode=Node(value)
        if self.head == None:
            self.head=newNode
            self.tail=self.head
            self.length+=1
        else:
            starting=self.head
            while starting.next != None:
                starting=starting.next
            starting.next=newNode
            self.tail=newNode
            self.length+=1
    def get(self,index):
        if index<0 or index>=self.length:
            return "Invalid Index"
        if self.head == None:
            return None
        if index == 0:
            return self.head
        start=self.head
        for loop in range(index):
            start=start.next
        return start
    def pop(self):
        if self.length == 0:
            return "No values present in the linked list"
        if self.length == 1:
            poppedValue=self.head
            self.head = None
            self.tail = self.head
            self.length=0
            return poppedValue
        lastNode=self.get(self.length-1)
        secondToLast=self.get(self.length-2)
        secondToLast.next=None
        self.tail=secondToLast
        self.length-=1
        return lastNode
    def reversal(self):
        if self.head == None or self.head.next == None:
            return self
        tempLinkedList=LinkedList()
        tempLinkedList.reversal()
        return "Reverse"




firstLinkedList=LinkedList()
print(firstLinkedList.reversal())
# firstLinkedList.add(12)
# # firstLinkedList.add(13)
# # firstLinkedList.add(14)
# # print(firstLinkedList.pop().value)
# # print(firstLinkedList.pop().value)
# # print(firstLinkedList.pop().value)
# # print("last one")


