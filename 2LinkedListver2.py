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

    def delete_node(self,position):
        temp = self.head
        if position == 0:
            self.head = temp.next
            temp = None
            return

        for i in range(position-1):#i =0 1
            temp = temp.next
            if temp is None:
                break

        if temp is None:
            return

        if temp.next is None:
            return

        next = temp.next.next
        temp.next = None
        temp.next = next

    def search(self,key):
        temp = self.head

        while temp is not None:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    def sorting(self,head):
        temp = head
        index = Node(None)
        if temp is None:
            return
        else:
            while temp is not None:
                index = temp.next
                while index is not None:
                    if temp.data > index.data:
                        temp.data,index.data = index.data,temp.data
                    index = index.next
                temp = temp.next


    def printList(self):
        temp = self.head
        while(temp):
            print(str(temp.data) + "->",end="")
            temp = temp.next

if __name__ == "__main__":
    link_obj = LinkedList()
    link_obj.head = Node(3)# 1 null

    link_obj.insertAtEnd(2)
    link_obj.insertAtEnd(1)
    link_obj.printList()

    while True:
        print("\n\t\t *****MENU*******\n\t\t")
        print("\n\t\t 1.Insert At the beginning\n\t\t")
        print("\n\t\t 2.Insert After\n\t\t")
        print("\n\t\t 3.Insert At the end\n\t\t")
        print("\n\t\t 4.Delete node\n\t\t")
        print("\n\t\t 5.Searching node\n\t\t")
        print("\n\t\t 6.Sorting node\n\t\t")
        option = int(input("Chose 1,2,3"))
        if option == 1:
            data = int(input("Please enter data to insert: "))
            link_obj.insertAtBegin(data)
            link_obj.printList()
        elif option == 2:
            data = int(input("Please enter data to insert: "))
            link_obj.insertAfter(link_obj.head.next,data)
            link_obj.printList()
        elif option == 3:
            data = int(input("Please enter data to insert: "))
            link_obj.insertAtEnd(data)
            link_obj.printList()
        elif option == 4:
            # data = int(input("Please enter data to delete: "))
            link_obj.delete_node(1)
            link_obj.printList()
        elif option == 5:
            data = int(input("Please enter data to find: "))
            link_obj.search(data)
            if link_obj.search(data):
                print(str(data) + " is found")
            else:
                print(str(data) + " is not found")
            link_obj.printList()
        elif option == 6:
            link_obj.sorting(link_obj.head)
            print("Sorted List: ")
            link_obj.printList()
    # second = Node(2)# 1 null 2 null
    # third = Node(3)#1 null 2 null 3 null
    #
    # link_obj.head.next = second
    # second.next = third
    # #fixed
    #
    # #insertatbeginning
    # link_obj.insertAtBegin(111)
    #
    # # insertAfter
    # link_obj.insertAfter(link_obj.head.next, 22222)
    #
    # link_obj.insertAtBegin(0)
    # link_obj.insertAtBegin(20)
    #
    #
    # #insertAtEnd
    # link_obj.insertAtEnd(10000)
    #
    # print("Original Linked list: ")
    # link_obj.printList()
    #
    # print("\nAfter Deleting an element: ")
    # link_obj.delete_node(7)
    # link_obj.printList()
    # print("\n")
    #
    #
    # #searching
    # item_to_find = 22222
    # if link_obj.search(item_to_find):
    #     print(str(item_to_find) + " is found")
    # else:
    #     print(str(item_to_find) + " is not found")


