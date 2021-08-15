class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def deleteNode(self, key):
        # Save the head first
        temp = self.head

        if(temp is not None):
            if(temp.data == key):
                self.head = temp.next
                temp = None
                return

        while(temp is not None):
            if(temp.data == key):
                break
            prev = temp
            temp = temp.next

        if(temp == None):
            return

        prev.next = temp.next
        temp = None

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end= ' ')
            temp = temp.next

    def removeDuplicates(self):
        temp = self.head
        if temp is None:
            return
        while temp.next is not None:
            if temp.data == temp.next.data:
                new = temp.next.next

                # We need to invalidate temp.next first before assigning new
                # Else temp.next would point to 2 nodes instead of just 1
                temp.next = None
                temp.next = new
            else:
                temp = temp.next
        return self.head
