class Node:
    def __init__(self,data):    #the confusion i had was how can we even make change to a variable that is already defined in the code.
        self.data = data        #But it turned out we can and i have done it as well(In current.next=newNode). so this is just a new node which is made specifically to get inserted at the end. 
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next


# This insert function adds or inserts the new node at the very end ONE BY ONE
    def insert(self,head,data): 
        newNode=Node(data)        # It firstly creates the node with the data as data.
        if not head:              # this checks if the linked list has any elements or not . if head is none or null it means that it does not have any element so, 
            return newNode        # WE return newNode here because whatever we return it gets stored in the head.
        current=head              # Here we c=have just created a variable which will iterate through the whole list .
        while current.next:
            current=current.next
        current.next=newNode      # After iterating when it reaches the last node. it will insert the newNode there.
        return head               # And then after all the insertion is done we return the head to the head so that it can traaverse to do some functions.
        
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    #This is the head variable that points towards the first node of linked list.And this calls the insert function.


mylist.display(head) 	  







