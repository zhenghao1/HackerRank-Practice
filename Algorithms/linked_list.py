class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def get(self, index):
        count = 0
        current = self.head
        while(current):
            if(count == index):
                return current.data
            count += 1
            current = current.next

        assert(False)
        return 0

    # Checks for existence of an element
    def contains(self, key, recursive=False):
        if recursive:
            return self.containsRecursive(self.head, key)
        return self.containsIterative(key)

    def containsIterative(self, key):
        current = self.head
        while(current):
            if(current.data == key):
                return True
            current = current.next

        return False

    def containsRecursive(self, node, key):
        if (node is None):
            return False
        if (node.data == key):
            return True

        return self.containsRecursive(node.next, key)

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def detectLoop(self):
        loop_detected = False
        slow = self.head
        fast = self.head
        while(slow and fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                loop_detected = True
                break
        return loop_detected

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
            if(temp.next is None):
                print(temp.data, end='\n')
            else:
                print(temp.data, end= ' -> ')
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

    def getLength(self, recursive=False):
        if recursive:
            return self.getLengthRecursive(self.head)
        return self.getLengthIterative(self.head)

    def getLengthIterative(self, node):
        count = 0
        current = node
        while(current):
            count += 1
            current = current.next
        return count

    def getLengthRecursive(self, node):
        if (not node):
            return 0
        else:
            return 1 + self.getLengthRecursive(node.next)

