# Question: Find nth node from the last in a linked list

# ================= NODE =================
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# ================= LINKED LIST =================
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newNode

    def __str__(self):
        temp = self.head
        result = ""
        while temp:
            result += str(temp.value) + " -> "
            temp = temp.next
        return result + "None"


# ================= FUNCTION =================
def nthToLast(ll, n):
    pointer1 = ll.head        # pointer 1 dari depan
    pointer2 = ll.head        # pointer 2 dari depan

    for i in range(n):        # geser pointer2 n langkah
        if pointer2 is None:
            return None
        pointer2 = pointer2.next

    while pointer2:           # jalan bareng
        pointer1 = pointer1.next
        pointer2 = pointer2.next

    return pointer1


# ================= MAIN =================
ll = LinkedList()

# Data manual (biar jelas, tidak random)
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)

print("Linked List:", ll)   # 10 -> 20 -> 30 -> 40 -> 50 -> None

result = nthToLast(ll, 2)

if result:
    print("Hasil:", result.value)   # Output: 40
else:
    print("None")