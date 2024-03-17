class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummynode= ListNode(0)
        current=dummynode
        carry=0

        while l1!= None or l2 != None or carry !=0:
            l1value = l1.val if l1 else 0
            l2value = l2.val if l2 else 0
            sum= l1value+l2value+carry
            carry = sum //10 
            current.next=  ListNode(sum%10) 
            current= current.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None

        return dummynode.next 





    

        