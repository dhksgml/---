
class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

memory = []
root = None
soldItemAry = ['츄파춥스','삼다수','츄파춥스','삼각김밥','바나나맛우유','도시락','코카콜라','바나나맛우유','츄파춥스',
            '레쓰비캔커피','바나나맛우유','코카콜라','도시락','츄파춥스','삼각김밥','바나나맛우유','코카콜라','코카콜라','도시락','츄파춥스']


print("오늘 판매된 물건(중복O)-->",soldItemAry)
print()

def preorder(node):
    if node == None:
        return
    print(node.data, end = ' ')
    preorder(node.left)
    preorder(node.right)

node = TreeNode()
node.data = soldItemAry[0]
root = node
memory.append(node)

for soldItem in soldItemAry[1:]:
    name = soldItem
    node = TreeNode()
    node.data = name

    current = root
    while True:
        if name == current.data:
            break
        else:
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
print('이진 탐색 트리 구성 완료!')
print()

print("오늘 판매된 종류(중복X)-->",end=' ')
preorder(root)

