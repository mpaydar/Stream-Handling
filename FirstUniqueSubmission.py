import random

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class Bucket:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.previous = self.tail
            self.tail = node

class FirstUnique:
    def __init__(self, nums):
        self.hashMap = [[0, False, None, Bucket()] for _ in range(100)]
        self.unique_head = None
        self.unique_tail = None
        self.a = random.randint(1, 99)
        self.b = random.randint(0, 99)

        for num in nums:
            self.add(num)

    def add(self, v):
        N = 100
        hashValue = (self.a * v + self.b) % N

        # Check if value already exists in the unique list
        node = self.hashMap[hashValue][2]
        while node is not None:
            if node.value == v:
                self.hashMap[hashValue][0] += 1
                # Remove node from unique list if occurrences become 2 or more
                if self.hashMap[hashValue][0] >= 2:
                    if node == self.unique_head:
                        self.unique_head = node.next
                        if self.unique_head:
                            self.unique_head.previous = None
                    elif node == self.unique_tail:
                        self.unique_tail = node.previous
                        if self.unique_tail:
                            self.unique_tail.next = None
                    else:
                        if node.previous:
                            node.previous.next = node.next
                        if node.next:
                            node.next.previous = node.previous
                return

            node = node.next

        # If value is not in the unique list, add it
        new_node = Node(v)
        self.hashMap[hashValue][0] += 1
        self.hashMap[hashValue][1] = True
        self.hashMap[hashValue][2] = new_node

        if self.unique_head is None:
            self.unique_head = new_node
            self.unique_tail = new_node
        else:
            self.unique_tail.next = new_node
            new_node.previous = self.unique_tail
            self.unique_tail = new_node

        # Append node to bucket's linked list
        self.hashMap[hashValue][3].append(new_node)

    def showFirstUnique(self):
        if self.unique_head:
            return self.unique_head.value
        return -1

    def print_stream(self):
        index = self.unique_head
        while index:
            print(f'{index.value}', end=' -> ')
            index = index.next
        print("")
