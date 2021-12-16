
class Node() :
    def __init__(self):
        self.data = None
        self.link = None


def printNodes(start) :

    current = start

    if current == None:
        return

    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()

def makeSimpleLinkedList(nameHeight):
    global memory, head, pre, current
    printNodes(head)

    node = Node()
    node.data = nameHeight
    memory.append(node)

    if head == None:
        head = node
        return

    if head.data[1] > nameHeight[1]:
        node.link = head
        head = node
        return

    current = head
    while current.link != None:
        pre = current
        current = current.link
        if head.data[1] > nameHeight[1]:
            pre.link = node
            node.link = current
            return

    current.link = node


memory = []
head, current, pre = None, None, None
dataArray = [['지민',180],['정국',177],['뷔',183],['슈가',175],['진',179]]

if __name__ == "__main__":

    for data in dataArray:
        makeSimpleLinkedList(data)

    printNodes(head)














            
            




