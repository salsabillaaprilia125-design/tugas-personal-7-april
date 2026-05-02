class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        # Jika list kosong
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
            return

        tail = self.head.prev

        tail.next = new_node
        new_node.prev = tail
        new_node.next = self.head
        self.head.prev = new_node

    def prepend(self, data):
        self.append(data)
        self.head = self.head.prev

    def display(self):
        if not self.head:
            print("List kosong")
            return
        
        temp = self.head
        result = []

        while True:
            result.append(str(temp.data))
            temp = temp.next
            if temp == self.head:
                break

        print(" <-> ".join(result) + " (kembali ke head)")


# Testing
cdll = CircularDoublyLinkedList()
cdll.append(1)
cdll.append(2)
cdll.append(3)

cdll.display()