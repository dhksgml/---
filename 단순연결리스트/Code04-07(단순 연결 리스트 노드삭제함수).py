class Node():
    def __init__ (self):
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
    print()

def deleteNode(deleteData):
    global memory,head,current,pre

    if head.data == deleteData:
        current = head
        head = head.link
        del(current)
        print("#첫 노드가 삭제됨#")
        return
    

    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == deleteData:
            pre.link = current.link
            del(current)
            print("#중간 노드가 삭제됨#")
            return
    print("# 삭제된 노드가 없음 #")

def insertNode(findData, insertData):
    global memory, head, curent, pre

    #첫 번째 노드 삽입
    if head.data == findData:
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return

    current = head
    #중간 노드 삽입
    while current.link != None:
        pre = current
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return
        
    #마지막 노드 삽입
    node=Node()
    node.data = insertData
    current.link = node

memory = []
head, current, pre = None,None,None
dataArray = ["다현","정연","쯔위","사나","지효"]

if __name__ == "__main__":

    node = Node()
    node.data = dataArray[0]
    head = node
    memory.append(node)


    
    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)

    print("현재 단순 연결 리스트 상태:",end=" ")
    printNodes(head)
    print("")
    
##    insertNode("다현","화사")
##    printNodes(head)
##
##    insertNode("사나","솔라")
##    printNodes(head)
##
##    insertNode("재남","문별")
##    printNodes(head)

    deleteNode("다현")
    printNodes(head)

    deleteNode("쯔위")
    printNodes(head)

    deleteNode("지효")
    printNodes(head)

    deleteNode("재남")
    printNodes(head)
    
