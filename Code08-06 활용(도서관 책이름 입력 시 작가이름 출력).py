import random

class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

##def preorder(node):
##    if node == None:
##        return
##    print(node.data, end = '->')
##    preorder(node.left)
##    preorder(node.right)

memory = []
rootBook, rootAuth = None, None
bookAry = [['어린왕자', '생떽쥐베리'], ['이방인', '까뮈'], ['부활', '톨스토이'],
           ['신곡', '단테'],['돈키호테','세르반테스'],['동물농장','조지오웰'],
           ['데미안','헤르만헤세'],['파우스트','괴테'],['대지','펄벅']]



random.shuffle(bookAry)
##print(bookAry)

node = TreeNode()
node.data = bookAry[0]
rootBook = node
memory.append(node)

for book in bookAry[1:]:
    name = book
    node = TreeNode()
    node.data = name

    current = rootBook
    while True:
        if name < current.data:
            if current.left == None:
                current.left = node
                break
            current = current.left
        else:
            if current.right == None:
                current.right = node
                break
            current = current.right
            
    memory.append(node)
print('책-작가 이름 트리 구성 완료!')

node = TreeNode()
node.data = bookAry[0]
rootAuth = node
memory.append(node)

for book in bookAry[1:]:
    name = book
    node = TreeNode()
    node.data = name

    current = rootAuth
    while True:
        if name[1] < current.data[1]:
            if current.left == None:
                current.left = node
                break
            current = current.left
        else:
            if current.right == None:
                current.right = node
                break
            current = current.right
            
    memory.append(node)
print('작가-책 이름 트리 구성 완료!')

##preorder(rootAuth)
##print()

while True:
    print()
    menu = int(input("메뉴선택: 책이름 검색(1), 작가이름 검색(2), 데이터 추가(3), 데이터 삭제(4), exit(5) -->"))

    if menu == 5:
        break

    #책-작가 검색
    if menu == 1:

        findName = input('검색할 책이름-->')

        root = rootBook
        current = root   
        while True:
            if findName == current.data[0]:
                
                print("책이름:",findName,end=' ')
                print("작가이름:",current.data[1])
                findYN = True
                break
            elif findName < current.data[0]:
                if current.left == None:
                    print(findName, '이(가) 목록에 없음')
                    break
                current = current.left

            else:
                if current.right == None:
                    print(findName, '이(가) 목록에 없음')
                    break
                current = current.right

    #작가-책 검색
    if menu == 2:

        findName = input('검색할 작가이름-->')

        root = rootAuth
        current = root
        while True:
            if findName == current.data[1]:
                
                print("작가이름:",findName,end=' ')
                print("책이름:",current.data[0])
                findYN = True
                break
            elif findName < current.data[1]:
                if current.left == None:
                    print(findName, '이(가) 목록에 없음')
                    break
                current = current.left

            else:
                if current.right == None:
                    print(findName, '이(가) 목록에 없음')
                    break
                current = current.right

    #데이터 추가
    if menu == 3:
        addBook = input('추가할 책이름:')
        addAuth = input('추가할 작가이름:')
        addData = [addBook,addAuth]

        node = TreeNode()
        node.data = addData

        current = rootBook
        while True:
            if addData[0] == current.data[0]:
                print('이미 데이터가 있습니다.')
                break
            else:
                if addData[0] < current.data[0]:
                    if current.left == None:
                        current.left = node
                        break
                    current = current.left

                else:
                    if current.right == None:
                        current.right = node
                        break
                    current = current.right
                memory.append(node)

        current = rootAuth
        while True:
            if addData[1] == current.data[1]:
                
                break
            else:
                if addData[1] < current.data[1]:
                    if current.left == None:
                        current.left = node
                        break
                    current = current.left

                else:
                    if current.right == None:
                        current.right = node
                        break
                    current = current.right
            memory.append(node)

    #데이터 삭제
    if menu == 4:
        deleteBook = input('삭제할 책이름:')
        deleteAuth = input('삭제할 작가이름:')
        deleteData = [deleteBook,deleteAuth]

        current = rootBook
        parent = None

        while True:
            if deleteData[0] == current.data[0]:
                if current.left == None and current.right == None:
                    if parent.left == current:
                        parent.left = None
                    else:
                        parent.right = None
                    del(current)

                elif current. left != None and current.right == None:
                    if parent.left == current:
                        parent.left = current.left
                    else:
                        parent.right = current.left
                    del(current)

                elif current.left == None and current.right != None:
                    if parent.left == current:
                        parent.left = current.right
                    else:
                        parent.right = current.right
                    del(current)
                print(deleteData,'이(가) 삭제됨.')
                break
            elif deleteData[0] < current.data[0]:
                if current.left == None:
                    print(deleteData, '이(가) 트리에 없음')
                    break
                parent = current
                current = current.left
            else:
                if current.right == None:
                    print(deleteData, '이(가) 트리에 없음')
                    break
                parent = current
                current = current.right


        current = rootAuth
        parent = None

        while True:
            if deleteData[1] == current.data[1]:
                if current.left == None and current.right == None:
                    if parent.left == current:
                        parent.left = None
                    else:
                        parent.right = None
                    del(current)

                elif current. left != None and current.right == None:
                    if parent.left == current:
                        parent.left = current.left
                    else:
                        parent.right = current.left
                    del(current)

                elif current.left == None and current.right != None:
                    if parent.left == current:
                        parent.left = current.right
                    else:
                        parent.right = current.right
                    del(current)
                break
            elif deleteData[1] < current.data[1]:
                if current.left == None:
                    
                    break
                parent = current
                current = current.left
            else:
                if current.right == None:
                    
                    break
                parent = current
                current = current.right
        
