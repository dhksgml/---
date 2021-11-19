import os

path = "C:/Program Files/Common Files"

fileAry = []

for (root, dirs, files) in os.walk(path):
    if len(files) > 0:
        for file_name in files:
            fileAry.append(file_name)


class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

memory = []
root = None

node = TreeNode()
node.data = fileAry[0]
root = node
memory.append(node)


doubleFileAry = []


for file in fileAry[1:]:
    name = file
    node = TreeNode()
    node.data = name

    current = root
    while True:
        if name == current.data:
            if current.data not in doubleFileAry:
                doubleFileAry.append(current.data)
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
        
print("C:/Program Files/Common Files/및 그 하위 디렉터리의 중복된 파일 목록 -->", doubleFileAry)
