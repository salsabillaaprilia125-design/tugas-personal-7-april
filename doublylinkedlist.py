class Node:
    def __init__(self, value=None):
        self.value = value        # Menyimpan data
        self.next = None          # Pointer ke node berikutnya
        self.prev = None          # Pointer ke node sebelumnya


class DoublyLinkedList:
    def __init__(self):
        self.head = None          # Node pertama
        self.tail = None          # Node terakhir

    def __iter__(self):
        node = self.head          # Mulai dari head
        while node:
            yield node            # Mengembalikan node satu per satu
            node = node.next      # Pindah ke node berikutnya

    # Membuat Doubly Linked List
    def createDLL(self, nodeValue):
        node = Node(nodeValue)    # Membuat node pertama
        node.prev = None
        node.next = None
        self.head = node          # Head = node
        self.tail = node          # Tail = node
        return "The DLL is created Successfully"
    
    
    # Menambahkan node
    def insertNode(self, nodeValue, location):
        if self.head is None:
            print("The node cannot be inserted")
        else:
            newNode = Node(nodeValue)   # Node baru

            if location == 0:           # Insert di depan
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode

            elif location == 1:         # Insert di belakang
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode

            else:                       # Insert di tengah
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode
    
    # Traversal maju
    def traverseDLL(self):
        if self.head is None:
            print("There is not any element to traverse")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)   # Print dari depan
                tempNode = tempNode.next
    
    # Traversal mundur
    def reverseTraversalDLL(self):
        if self.head is None:
            print("There is not any element to traverse")
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)   # Print dari belakang
                tempNode = tempNode.prev

    # Search data
    def searchDLL(self, nodeValue):
        if self.head is None:
            return "There is not any element in the list"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value   # Jika ketemu
                tempNode = tempNode.next
            return "The node does not exist in this list"

    # Hapus node
    def deleteNode(self,location):
        if self.head is None:
            print("There is not any element in DLL")
        else:
            if location == 0:           # Hapus depan
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None

            elif location == 1:         # Hapus belakang
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None

            else:                       # Hapus tengah
                curNode = self.head
                index = 0
                while index < location - 1:
                    curNode = curNode.next
                    index += 1
                curNode.next = curNode.next.next
                curNode.next.prev = curNode

            print("The node has been successfully deleted")

    # Hapus seluruh list
    def deleteDLL(self):
        if self.head is None:
            print("There is not any node in DLL")
        else:
            tempNode = self.head
            while tempNode:
                tempNode.prev = None   # Hapus koneksi prev
                tempNode = tempNode.next
            self.head = None
            self.tail = None
            print("The DLL has been successfully deleted")


# ===================== MAIN =====================

doubyLL = DoublyLinkedList()       # Membuat objek
doubyLL.createDLL(5)               # [5]

doubyLL.insertNode(0,0)            # Depan → [0,5]
doubyLL.insertNode(2,1)            # Belakang → [0,5,2]
doubyLL.insertNode(6,2)            # Tengah → [0,5,6,2]

print([node.value for node in doubyLL])   # Output: [0, 5, 6, 2]

doubyLL.deleteDLL()               # Hapus semua node

print([node.value for node in doubyLL])   # Output: []
