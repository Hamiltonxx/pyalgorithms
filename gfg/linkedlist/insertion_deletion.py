class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None 

    def deleteNode(self,key):
        temp = self.head 
        if temp!=None and temp.data==key:
            self.head = temp.next
            return 
        while temp.next:
            if temp.next.data == key:
                temp.next = temp.next.next
                break 
            temp = temp.next

    #从头开始，遍历链表
    def printList(self):
        temp = self.head 
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second; # Link first node with second 
    second.next = third; # Link second node with the third node
    ''' 
    llist.head        second              third 
         |                |                  | 
         |                |                  | 
    +----+------+     +----+------+     +----+------+ 
    | 1  |  o-------->| 2  |  o-------->|  3 | null | 
    +----+------+     +----+------+     +----+------+  
    '''
    llist.deleteNode(2)

    llist.printList()
