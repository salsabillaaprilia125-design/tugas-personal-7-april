# Question 1 - Remove Dups:
# Write a code to remove duplicates from an unsorted linked list.


# ================= NODE =================
class Node:
    def __init__(self, value):
        self.value = value        # Menyimpan data
        self.next = None          # Pointer ke node berikutnya


# ================= LINKED LIST =================
class LinkedList:
    def __init__(self):
        self.head = None          # Node pertama

    def append(self, value):
        newNode = Node(value)     # Membuat node baru

        if self.head is None:     # Jika list kosong
            self.head = newNode   # Node jadi head
        else:
            temp = self.head      # Mulai dari head
            while temp.next:      # Cari node terakhir
                temp = temp.next
            temp.next = newNode   # Tambahkan di akhir

    def __str__(self):
        temp = self.head          # Mulai dari head
        result = ""               # Menyimpan hasil

        while temp:               # Loop semua node
            result += str(temp.value) + " -> "   # Tambahkan ke string
            temp = temp.next      # Pindah ke node berikutnya

        return result + "None"    # Akhiran list


# ================= REMOVE DUPLICATES =================
def removeDups(ll):
    if ll.head is None:           # Jika list kosong
        return
    
    currentNode = ll.head         # Mulai dari node pertama
    visited = set([currentNode.value])   # Simpan nilai pertama

    while currentNode.next:       # Selama masih ada node berikutnya
        if currentNode.next.value in visited:   # Jika duplikat
            currentNode.next = currentNode.next.next   # HAPUS node
        else:
            visited.add(currentNode.next.value)  # Simpan nilai baru
            currentNode = currentNode.next       # Pindah ke node berikutnya

    return ll


# ================= MAIN =================
ll = LinkedList()                 # Membuat linked list

ll.append(3)                     # Tambah 3
ll.append(5)                     # Tambah 5
ll.append(3)                     # Duplikat
ll.append(7)                     # Tambah 7
ll.append(5)                     # Duplikat
ll.append(1)                     # Tambah 1

print("Sebelum:", ll)            # Output: 3 -> 5 -> 3 -> 7 -> 5 -> 1 -> None

removeDups(ll)                  # Menghapus duplikat

print("Sesudah:", ll)            # Output: 3 -> 5 -> 7 -> 1 -> None