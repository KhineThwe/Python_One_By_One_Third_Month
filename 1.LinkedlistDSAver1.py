#Data Structure
#Linked List DSA
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
#data<-data
#next<-Null

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegin(self,n_data):
        new_node = Node(n_data)#0 null

        new_node.next = self.head
        self.head = new_node

    def insertAtEnd(self,n_data):
        new_node = Node(n_data)#10000 nulll

        temp = self.head
        while(temp.next!=None):
            temp = temp.next

        temp.next = new_node


    def insertAfter(self,prev_node,n_data):

        new_node = Node(n_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print(str(temp.data) + "->",end="")
            temp = temp.next

if __name__ == "__main__":
    link_obj = LinkedList()
    link_obj.head = Node(1)# 1 null
    second = Node(2)# 1 null 2 null
    third = Node(3)#1 null 2 null 3 null

    link_obj.head.next = second
    second.next = third
    #fixed

    #insertatbeginning
    link_obj.insertAtBegin(111)

    # insertAfter
    link_obj.insertAfter(link_obj.head.next, 22222)

    link_obj.insertAtBegin(0)
    link_obj.insertAtBegin(20)


    #insertAtEnd
    link_obj.insertAtEnd(10000)

    link_obj.printList()


