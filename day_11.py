from collections import defaultdict
import file_reader

FILE_NAME = 'files/day11.txt'

# Create a Node class to create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create a LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    # Method to add a node at the beginning of the LL
    def insertAtBegin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Method to add a node at any index
    # Indexing starts from 0.
    def insertAtIndex(self, data, current_node):
        if current_node is None:
            self.insertAtBegin(data)
            return

        if current_node is not None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("Index not present")

    # Method to add a node at the end of LL
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    # Update node at a given position
    def updateNode(self, val, current_node):
        if current_node is not None:
            current_node.data = val
        else:
            print("Index not present")

    # Method to remove first node of linked list
    def remove_first_node(self):
        if self.head is None:
            return

        self.head = self.head.next

    # Method to remove last node of linked list
    def remove_last_node(self):
        if self.head is None:
            return

        # If there's only one node
        if self.head.next is None:
            self.head = None
            return

        # Traverse to the second last node
        current_node = self.head
        while current_node.next and current_node.next.next:
            current_node = current_node.next

        current_node.next = None

    # Method to remove a node at a given index
    def remove_at_index(self, index):
        if self.head is None:
            return

        if index == 0:
            self.remove_first_node()
            return

        current_node = self.head
        position = 0
        while current_node is not None and current_node.next is not None and position + 1 != index:
            position += 1
            current_node = current_node.next

        if current_node is not None and current_node.next is not None:
            current_node.next = current_node.next.next
        else:
            print("Index not present")

    # Method to remove a node from the linked list by its data
    def remove_node(self, data):
        current_node = self.head

        # If the node to be removed is the head node
        if current_node is not None and current_node.data == data:
            self.remove_first_node()
            return

        # Traverse and find the node with the matching data
        while current_node is not None and current_node.next is not None:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

        # If the data was not found
        print("Node with the given data not found")

    # Print the size of the linked list
    def sizeOfLL(self):
        size = 0
        current_node = self.head
        while current_node:
            size += 1
            current_node = current_node.next
        return size

    # Print the linked list
    def printLL(self):
        current_node = self.head
        while current_node:
            print(current_node.data,end=' ')
            current_node = current_node.next
        print()
        
    def get(self, index):
        current_node = self.head
        position = 0
        while current_node is not None and position != index:
            position += 1
            current_node = current_node.next

        if current_node is not None:
            return current_node
        else:
            print("Index not present")

def part_one():

    stones = LinkedList()
    for stone in file_reader.read_file_as_str(FILE_NAME).split(' '):
        stones.insertAtEnd(stone)

    loop_count = 25
        
    while loop_count != 0:
        stone: Node = stones.head

        while stone is not None:
            if stone.data == '0':
                stone.data = '1'
            elif len(stone.data)%2 == 0:
                
                left = stone.data[:len(stone.data)//2]
                right = stone.data[-len(stone.data)//2:]
                
                stones.updateNode(left, stone)
                
                stones.insertAtIndex(str(int(right)), stone)
                stone = stone.next
            else:
                stone.data = str(int(stone.data)*2024)
                
            stone = stone.next
            
        loop_count -= 1
    
    return stones.sizeOfLL()

def part_two():
    
    d = defaultdict(int)
    
    for stone in file_reader.read_file_as_str(FILE_NAME).split(' '):
        d[stone] = 1

    
    loop_count = 75
        
    while loop_count != 0:
        new_d = d.copy()
        
        for value, count in d.items():
            
            if value == '0':
                new_d['0'] -= count
                new_d['1'] += count
            elif len(value)%2 == 0:
                
                left = value[:len(value)//2]
                right = str(int(value[-len(value)//2:]))
                
                new_d[value] -= count
                new_d[left] += count
                new_d[right] += count
            else:
                new_d[value] -= count
                new_d[str(int(value)*2024)] += count
        
        loop_count -= 1
        d = defaultdict(int)
        
        for v,i in new_d.items():
            if i > 0:
                d[v] = i
    
    return sum(d.values())

print(f"Part One: {part_one()}")
print(f"Part Two: {part_two()}")