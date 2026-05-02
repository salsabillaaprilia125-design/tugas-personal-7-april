# Question 3:
# Partition linked list berdasarkan nilai x
# (nilai < x di depan, nilai >= x di belakang)

# ================= NODE =================
class Node:
    def __init__(self, value):
        self.value = value        # Menyimpan data di node
        self.next = None          # Pointer ke node berikutnya


# ================= LINKED LIST =================
class LinkedList:
    def __init__(self):
        self.head = None          # Node pertama
        self.tail = None          # Node terakhir

    def append(self, value):
        newNode = Node(value)     # Membuat node baru
        if self.head is None:     # Jika list kosong
            self.head = newNode   # Node jadi head
            self.tail = newNode   # Node juga jadi tail
        else:
            self.tail.next = newNode  # Sambungkan ke belakang
            self.tail = newNode       # Update tail

    def __str__(self):
        temp = self.head          # Mulai dari head
        result = ""
        while temp:               # Loop semua node
            result += str(temp.value) + " -> "   # Gabungkan ke string
            temp = temp.next      # Pindah ke node berikutnya
        return result + "None"    # Akhiran list


# ================= PARTITION FUNCTION =================
def partition(ll, x):
    curNode = ll.head           # Mulai dari node pertama
    ll.tail = ll.head           # Set tail awal

    while curNode:
        nextNode = curNode.next # Simpan node berikutnya (biar tidak hilang)
        curNode.next = None     # Putuskan sementara koneksi

        if curNode.value < x:   # Jika nilai lebih kecil dari x
            curNode.next = ll.head  # Masukkan ke depan
            ll.head = curNode       # Update head
        else:                   # Jika nilai >= x
            ll.tail.next = curNode  # Tambahkan ke belakang
            ll.tail = curNode       # Update tail

        curNode = nextNode      # Lanjut ke node berikutnya

    if ll.tail:                # Jika tail ada
        ll.tail.next = None    # Pastikan tidak nyambung lagi


# ================= MAIN =================
ll = LinkedList()             # Membuat linked list

ll.append(3)                  # Tambah 3
ll.append(5)                  # Tambah 5
ll.append(8)                  # Tambah 8
ll.append(5)                  # Tambah 5
ll.append(10)                 # Tambah 10
ll.append(2)                  # Tambah 2
ll.append(1)                  # Tambah 1

print("Sebelum:", ll)        # Output: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 -> None

partition(ll, 5)             # Pisahkan berdasarkan x = 5

print("Sesudah:", ll)        # Output: 1 -> 2 -> 3 -> 5 -> 8 -> 5 -> 10 -> None