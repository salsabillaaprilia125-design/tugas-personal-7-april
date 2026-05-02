class Node:
    def __init__(self, value=None):
        self.value = value        # Menyimpan data
        self.next = None          # Pointer ke node berikutnya
        self.prev = None          # Pointer ke node sebelumnya


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None          # Node pertama
        self.tail = None          # Node terakhir

    def __iter__(self):
        node = self.head          # Mulai dari head
        while node:               
            yield node            # Mengembalikan node satu per satu
            node = node.next      # Pindah ke node berikutnya
            if node == self.tail.next:  # Berhenti jika kembali ke awal (circular)
                break

    # Membuat Circular Doubly Linked List
    def createCDLL(self, nodeValue):
        newNode = Node(nodeValue)     # Membuat node baru
        self.head = newNode           # Head = node baru
        self.tail = newNode           # Tail = node baru
        newNode.prev = newNode        # Prev menunjuk ke dirinya sendiri
        newNode.next = newNode        # Next menunjuk ke dirinya sendiri
        return "The CDLL is created successfully"

    # Menambahkan node
    def insertCDLL(self, value, location):
        if self.head is None:
            return "The CDLL does not exist"
        else:
            newNode = Node(value)     # Membuat node baru

            if location == 0:         # Insert di depan
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode

            elif location == 1:       # Insert di belakang
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode
                self.tail = newNode

            else:                     # Insert di tengah
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode

            return "The node has been successfully inserted"

    # Traversal (maju)
    def traversalCDLL(self):
        if self.head is None:
            print("There is not any node for traversal")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)     # Print nilai
                if tempNode == self.tail:
                    break
                tempNode = tempNode.next

    # Traversal (mundur)
    def reverseTraversalCDLL(self):
        if self.head is None:
            print("There is not any node for reverse traversal")
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)     # Print nilai dari belakang
                if tempNode == self.head:
                    break
                tempNode = tempNode.prev

    # Search data
    def searchCDLL(self, nodeValue):
        if self.head is None:
            return "There is not any node in CDLL"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value   # Jika ketemu
                if tempNode == self.tail:
                    return "The value does not exist in CDLL"
                tempNode = tempNode.next

    # Delete node
    def deleteNode(self, location):
        if self.head is None:
            print("There is not any node to delete")
        else:
            if location == 0:           # Hapus depan
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head

            elif location == 1:         # Hapus belakang
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail

            else:                       # Hapus tengah
                curNode = self.head
                index = 0
                while index < location - 1:
                    curNode = curNode.next
                    index += 1
                curNode.next = curNode.next.next
                curNode.next.prev = curNode

            print("The node has been successfully deleted")

    # Delete seluruh list
    def deleteCDLL(self):
        if self.head is None:
            print("There is not any element to delete")
        else:
            self.tail.next = None
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
            print("The CDLL has been successfully deleted")


# ===================== MAIN PROGRAM =====================

circularDLL = CircularDoublyLinkedList()   # Membuat objek CDLL
circularDLL.createCDLL(5)                  # Buat node pertama → [5]

circularDLL.insertCDLL(0,0)                # Insert depan → [0,5]
circularDLL.insertCDLL(1,1)                # Insert belakang → [0,5,1]
circularDLL.insertCDLL(2,2)                # Insert tengah → [0,5,2,1]

print([node.value for node in circularDLL])  # Output: [0, 5, 2, 1]

circularDLL.deleteCDLL()                  # Hapus semua node

print([node.value for node in circularDLL])  # Output: []