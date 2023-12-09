class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail=None



    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail=new_node


    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.tail = new_node
            self.head=new_node
    
    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False
    
    def printLinkedList(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
    def remove_beginning(self):
        if self.head:
            removed_data = self.head.data
            if self.head.next:
                self.head = self.head.next
            else:
                self.head = None
                self.tail = None
            return removed_data
        return None
    
    def remove_at_end(self):
        if self.head:
            removed_data = self.tail.data
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                current_node = self.head
                while current_node.next != self.tail:
                    current_node = current_node.next
                current_node.next = None
                self.tail = current_node
            return removed_data
        return None
    
    def remove_at(self, data):
        current_node = self.head
        prev_node = None
        while current_node:
            if current_node.data == data:
                removed_data = current_node.data
                if prev_node:
                    prev_node.next = current_node.next
                    if current_node == self.tail:
                        self.tail = prev_node
                else:
                    self.head = current_node.next
                    if current_node == self.tail:
                        self.tail = None
                return removed_data
            prev_node = current_node
            current_node = current_node.next
        return None
   
def merge_sorted_lists(list1, list2):
    merged_list = LinkedList()
    
    # Check the number of nodes in each list
    if not (0 <= count_nodes(list1) <= 50 and 0 <= count_nodes(list2) <= 50):
        raise ValueError("Number of nodes in each linked list should be between 0 and 50.")

    current1 = list1.head
    current2 = list2.head

    # If both linked lists have elements
    while current1 and current2:
        # Check the value range of each node
        if -100 <= current1.data <= 100 and -100 <= current2.data <= 100:
            if current1.data < current2.data:
                merged_list.insert_at_end(current1.data)
                current1 = current1.next
            else:
                merged_list.insert_at_end(current2.data)
                current2 = current2.next
        else:
            raise ValueError("Node value must be between -100 and 100.")

    # If any linked list has remaining elements
    while current1:
        # Check the value range of each node
        if -100 <= current1.data <= 100:
            merged_list.insert_at_end(current1.data)
            current1 = current1.next
        else:
            raise ValueError("Node value must be between -100 and 100.")

    while current2:
        # Check the value range of each node
        if -100 <= current2.data <= 100:
            merged_list.insert_at_end(current2.data)
            current2 = current2.next
        else:
            raise ValueError("Node value must be between -100 and 100.")

    return merged_list

def count_nodes(linked_list):
    count = 0
    current_node = linked_list.head
    while current_node:
        count += 1
        current_node = current_node.next
    return count

# Example usage:
list1 = LinkedList()
list1.insert_at_end(1)
list1.insert_at_end(2)
list1.insert_at_end(4)


list2 = LinkedList()
list2.insert_at_end(1)
list2.insert_at_end(3)
list2.insert_at_end(4)

merged_list = merge_sorted_lists(list1, list2)

print("Merged List:")
merged_list.printLinkedList()

merged_list.remove_beginning()
merged_list.remove_at_end()
merged_list.remove_at(3)
merged_list.insert_at_end(5)
merged_list.insert_at_end(6)

print("New Merged List:")
merged_list.printLinkedList()