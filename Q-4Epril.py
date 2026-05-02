# Question 4 - Sum Lists
# Menjumlahkan dua linked list (digit per node)

# ================= NODE =================
class Node:
    def __init__(self, value):
        self.value = value        # Menyimpan angka
        self.next = None          # Pointer ke node berikutnya


# ================= LINKED LIST =================
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        newNode = Node(value)     # Membuat node baru
        if self.head is None:     # Jika kosong
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode  # Tambah ke belakang
            self.tail = newNode

    def __str__(self):
        temp = self.head
        result = ""
        while temp:
            result += str(temp.value) + " -> "
            temp = temp.next
        return result + "None"


# ================= SUM FUNCTION =================
def sumList(llA, llB):
    n1 = llA.head
    n2 = llB.head
    carry = 0
    ll = LinkedList()

    while n1 or n2:
        result = carry          # Mulai dari carry

        if n1:
            result += n1.value  # Tambah nilai list A
            n1 = n1.next

        if n2:
            result += n2.value  # Tambah nilai list B
            n2 = n2.next

        ll.add(result % 10)     # Simpan digit terakhir
        carry = result // 10    # Ambil carry (PERBAIKAN)

    if carry:                   # Jika masih ada sisa carry
        ll.add(carry)

    return ll


# ================= MAIN =================
llA = LinkedList()
llA.add(7)
llA.add(1)
llA.add(6)   # 617

llB = LinkedList()
llB.add(5)
llB.add(9)
llB.add(2)   # 295

print("List A:", llA)
print("List B:", llB)

result = sumList(llA, llB)

print("Hasil :", result)   # 912 → 2 -> 1 -> 9