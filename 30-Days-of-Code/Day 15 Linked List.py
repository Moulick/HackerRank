class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:

    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next
#------------Only-this-part-is-needed------------#

    def insert(self, head, data):
        if head == None:
            head = Node(data)
# Moulick
        else:
            current = head
            while current.next != None:
                current = current.next
            current.next = Node(data)
        return head
#------------Only-this-part-is-needed------------#

mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
mylist.display(head)
