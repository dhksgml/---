class Node():
    def __init__(self):
        self.data = None
        self.link = None


def printNodes(start):
    current = start

    if current.link == None:
        return

    print(current.data, end=' ')
    #끝까지 반복
    while current.link != start:
        current = current.link
        print(current.data, end = ' ')
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
            node.link = current
            pre.link = node
            return

    node = Node()
    node.data = insertData
    current.link = node
    node.link = head
    

memory = []
head, current, pre = None, None, None
dataArray = ['다현','정연','쯔위','사나','지효']

if __name__ == "__main__":

    # 첫번째 노드
    node = Node()
    node.data = dataArray[0]
    head = node
    node.link = head
    memory.append(node)

    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        node.link = head
        memory.append(node)

    printNodes(head)

    insertNode("다현","화사")
    printNodes(head)

    insertNode("사나","솔라")
    printNodes(head)

    insertNode("재남","문별")
    printNodes(head)

        
    
