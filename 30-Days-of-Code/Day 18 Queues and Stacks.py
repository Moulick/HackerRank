import sys

#------------Only-this-part-is-needed------------#


class Solution:

    def __init__(self):
        self.items = []
        self.queue = []

    def pushCharacter(self, item):
        self.items.append(item)
        print(self.items)

    def enqueueCharacter(self, item):
        self.queue.insert(0, item)
        print(self.queue)
        # Moulick

    def popCharacter(self):
        print(self.items)
        return self.items.pop()

    def dequeueCharacter(self):
        print(self.queue)
        return self.queue.pop()
#------------Only-this-part-is-needed------------#

# read the string s
s = input()
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True

for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")
