# 链表之递归求解长度,递归查找元素和递归逆序
class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None 

    def push(self, data):
        node = Node(data)
        node.next = self.head 
        self.head = node 

    def printList(self):
        temp = self.head 
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def getCount(self):
        def getCountUtil(head):
            if not head:
                return 0
            return 1+getCountUtil(head.next)
        return getCountUtil(self.head)

    def search(self, data):
        def searchUtil(head):
            if not head:
                return False 
            if head.data == data:
                return True
            return searchUtil(head.next) 
        return searchUtil(self.head)

    def reverse(self):
        if self.head is None:
            return 
        def reverseUtil(curr,prev):
            if curr.next is None:
                self.head = curr 
                curr.next = prev 
                return 
            next = curr.next 
            curr.next = prev
            reverseUtil(next,curr)
        reverseUtil(self.head, None)


if __name__ == '__main__':
    llist = LinkedList()
    llist.push(1)
    llist.push(3)
    llist.push(1)
    llist.push(2)
    llist.push(1)
    print(f"LinkedList is: ")
    llist.printList()
    print(f"LinkedList Length is: {llist.getCount()}")
    print(f"3 in LinkedList: {llist.search(3)}")
    print(f"4 in LinkedList: {llist.search(4)}")

    llist.reverse()
    print("Reversed Linked List:")
    llist.printList()
