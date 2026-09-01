class Solution:
    def isPalindrome(self, head):
        a = []

        while head:
            a.append(head.val)
            head = head.next

        return a == a[::-1]