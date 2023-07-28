# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        # Create a dummy node to serve as the head of the result linked list

        # Pointer to the current node
        current = dummy

        # Variable to store the carry during addition
        carry = 0

        while l1 or l2 or carry:
        # Calculate the sum of the current digits and carry
            total = carry
        # Check if there is a digit in the first linked list
            if l1:
                total += l1.val
                l1 = l1.next
            
        # Check if there is a digit in the second linked list
            if l2:
                total += l2.val
                l2 = l2.next
        # Update the carry and create a new node with the sum

            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next


        # Return the head of the resulting linked list
        return dummy.next


            