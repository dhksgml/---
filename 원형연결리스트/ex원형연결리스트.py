class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):

    current = start

    if current.link == None:
        return

    print(current.data,end=' ')

    while current.link != start:
        current = current.link
        print(current.data, end=' ')
    print()


def insertNode(findData,insertData):
    global memory, head, current, pre

    if head.data == findData:
        node = Node()
        node.data = insertData
        node.link = head
        last = head
        while last.link != head:
            last = last.link
        last.link = node
        head = node
        return

    current = head
    while current.link != head:
        pre = current
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = insertData
            pre.link = node
            node.link = current
            return

    node = Node()
    node.data = insertData
    current.link = node
    node.link = head

def deleteNode(deleteData):
    global memory, head, current, pre

    if head.data == deleteData:
        current = head
        head = head.link
        last = head
        while last.link != current:
            last = last.link
        last.link = head
        del(current)
        return

    print("---제거할 데이터가 없습니다---")


memory = []
head, current, pre = None,None,None
dataArray = ['다현','정연','쯔위','사나','지효']




        
