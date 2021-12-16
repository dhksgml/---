import random

class Node():
    def __init__(self):
        self.data = None
        self.link = None


def printNodes(start):
    current = start

    if current.link == None:
        return

    print(current.data, end=' ')
    while current.link != start:
        current = current.link
        print(current.data, end = ' ')
    print()

def countPositiveNegative():
    global memory, head, current, pre

    positive, negative = 0, 0
    if head == None:
        return False

    current = head
    while True:
        if current.data > 0:
            positive += 1
        elif current.data < 0:
            negative += 1
        if current.link == head:
            break
        current = current.link

    return positive, negative

def makeZeroNumber(positive,negative):
    if positive > 0:
        reminder = 1
    elif negative < 0:
        reminder = 0

    current = head
    while True:
        current.data *= -1
        if current.link == head:
            break
        current = current.link
        




memory = []
head, current, pre = None, None, None

if __name__ == "__main__":


    dataArray = []
    for _ in range(7):
        dataArray.append(random.randint(-100,100))

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


    positiveCount, negativeCount = countPositiveNegative()
    print('양수 -->',positiveCount, '\t','음수-->',negativeCount)

    makeZeroNumber(positiveCount, negativeCount)
    printNodes(head)
    
