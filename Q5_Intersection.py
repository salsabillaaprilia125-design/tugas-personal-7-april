# Question 5 - Intersection
# Mencari node pertemuan (intersection) dari dua linked list

# ================= NODE =================
class Node:
    def __init__(self, value):
        self.value = value        # Menyimpan data
        self.next = None          # Pointer ke node berikutnya


# ================= LINKED LIST =================
class LinkedList:
    def __init__(self):
        self.head = None          # Node pertama
        self.tail = None          # Node terakhir

    def add(self, value):
        newNode = Node(value)     # Membuat node baru
        if self.head is None:     # Jika list kosong
            self.head = newNode   # Set head
            self.tail = newNode   # Set tail
        else:
            self.tail.next = newNode  # Sambungkan ke belakang
            self.tail = newNode       # Update tail

    def __len__(self):
        temp = self.head          # Mulai dari head
        count = 0                 # Hitung panjang
        while temp:               # Loop semua node
            count += 1
            temp = temp.next
        return count              # Kembalikan panjang list

    def __str__(self):
        temp = self.head
        result = ""
        while temp:
            result += str(temp.value) + " -> "   # Gabungkan nilai
            temp = temp.next
        return result + "None"


# ================= INTERSECTION FUNCTION =================
def intersection(llA, llB):

    # Jika tail berbeda → tidak mungkin ada intersection
    if llA.tail is not llB.tail:
        return None

    lenA = len(llA)               # Panjang list A
    lenB = len(llB)               # Panjang list B

    # Tentukan list yang lebih pendek & panjang
    shorter = llA if lenA < lenB else llB
    longer = llB if lenA < lenB else llA

    diff = abs(lenA - lenB)       # Selisih panjang

    longerNode = longer.head      # Pointer untuk list panjang
    shorterNode = shorter.head    # Pointer untuk list pendek

    # Geser pointer list panjang supaya sejajar
    for i in range(diff):
        longerNode = longerNode.next

    # Jalan bareng sampai ketemu node yang sama
    while shorterNode is not longerNode:
        shorterNode = shorterNode.next
        longerNode = longerNode.next

    return longerNode             # Node intersection


# ================= HELPER =================
def addSameNode(llA, llB, value):
    tempNode = Node(value)        # Membuat node yang SAMA

    llA.tail.next = tempNode      # Sambungkan ke list A
    llA.tail = tempNode

    llB.tail.next = tempNode      # Sambungkan ke list B
    llB.tail = tempNode


# ================= MAIN =================
llA = LinkedList()
llA.add(1)
llA.add(2)
llA.add(3)

llB = LinkedList()
llB.add(4)
llB.add(5)
llB.add(6)
llB.add(7)

# Membuat intersection (node yang sama dipakai dua list)
addSameNode(llA, llB, 11)
addSameNode(llA, llB, 14)

print("List A:", llA)
print("List B:", llB)

result = intersection(llA, llB)

# Menampilkan hasil
if result:
    print("Intersection di node:", result.value)
else:
    print("Tidak ada intersection")