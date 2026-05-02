class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        
        temp.next = new_node
        new_node.prev = temp

    def insert_at_position(self, pos, data):
        new_node = Node(data)

        # Insert di awal
        if pos == 1:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            return

        temp = self.head
        for _ in range(pos - 2):
            if not temp:
                print("Posisi melebihi panjang list")
                return
            temp = temp.next

        if not temp:
            print("Posisi melebihi panjang list")
            return

        new_node.next = temp.next
        new_node.prev = temp

        if temp.next:
            temp.next.prev = new_node
        
        temp.next = new_node

    def delete(self, data):
        temp = self.head

        while temp:
            if temp.data == data:
                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next
                
                if temp.next:
                    temp.next.prev = temp.prev
                return
            temp = temp.next

        print("Data tidak ditemukan")

    def search(self, data):
        temp = self.head
        pos = 1

        while temp:
            if temp.data == data:
                return pos
            temp = temp.next
            pos += 1

        return -1

    def display(self):
        temp = self.head
        result = []
        while temp:
            result.append(str(temp.data))
            temp = temp.next
        print(" <-> ".join(result))


# Testing
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)

dll.insert_at_position(2, 15)
dll.delete(20)

dll.display()
print("Posisi 30:", dll.search(30))