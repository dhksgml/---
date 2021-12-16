class Node():
    def __init__(self):
        self.data = None
        self.link = None


def printNodes(start):
    current = start
    if current == None:
        return
    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()


def makeSimpleLinkedList(nameEmail):
    global memory, head, current, pre

    node = Node()
    node.data = nameEmail
    memory.append(node)
    if head == None:
        head = node
        return

    if head.data[1] > nameEmail[1]:
        node.link = head
        head = node
        return

    current=head
    while current.link != None:
        pre = current
        current = current.link
        if current.data[1] > nameEmail[1]:
            pre.link = node
            node.link = current
            return
        
    current.link = node

memory = []
head, current, pre = None, None, None

if __name__ == "__main__":

    while True:
        name = input("이름-> ")
        if name == "" or None:
            break
        email = input("이메일-> ")
        makeSimpleLinkedList([name,email])
        printNodes(head)
