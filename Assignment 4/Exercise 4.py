#Exercise 4. Write deleteAtLocation function for a LL that takes as input an integer and deletes the node at that given location.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> " if current.next else "\n")
            current = current.next

    
    def deleteAtLocation(self, position):
        if self.head is None:  
            print("List is empty.")
            return

        
        if position == 0:
            self.head = self.head.next
            return

        
        current = self.head
        for i in range(position - 1):
            if current.next is None:  
                print("Position out of range.")
                return
            current = current.next

        
        if current.next is None:  
            print("Position out of range.")
            return

        
        current.next = current.next.next


ll = LinkedList()
ll.append(12)
ll.append(56)
ll.append(76)
ll.append(11)
ll.append(0)

print("Original List:")
ll.print_list()


ll.deleteAtLocation(0)
print("After deleting node at position 0:")
ll.print_list()


ll.deleteAtLocation(2)
print("After deleting node at position 2:")
ll.print_list()

