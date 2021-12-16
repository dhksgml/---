
#스택이 꽉 찼는지 확인
def isStackFull():
    global SIZE,stack,top
    if(top>=SIZE-1):
        return True
    else:
        return False

#스택이 비었는지 확인    
def isStackEmpty():
    global SIZE,stack,top
    if(top == -1):
        return True
    else:
        return False

#스택에 데이터 삽입
def push(data):
    global SIZE,stack,top
    if(isStackFull()):
        return
    top += 1
    stack[top] = data
    
#스택에서 데이터 삭제, 반환
def pop():
    global SIZE,stack,top
    if(isStackEmpty()):
        return None

    data = stack[top]
    stack[top] = None
    top -= 1
    return data
    

#스택 크기 지정, 초기화
SIZE = 100
stack = [None for _ in range(SIZE)]
top = -1


#외부 파일을 불러오기 위해 필요한 코드,
#진달래꽃.txt 파일을 읽기 모드로 UTF8 인코딩 방식으로 열어서, rfp라는 별명으로 사용하겠다는 의미
with open("진달래꽃.txt","r",encoding="UTF8") as rfp:
    lineAry = rfp.readlines() #파일을 읽어 lineAry에 저장

print("-------원본---------")
for line in lineAry: #lineAry에서 문자열 한 줄 씩 line에 저장
    print(line,end="") #한줄 출력
    push(line)  #stack에 한 줄 삽입
print()

print("-------거꾸로-------")
while True:
    line = pop()    #stack에서 데이터를 꺼내 line에 저장
    if(line == None):   #읽은 데이터가 None이면 stack이 비었다는 뜻, 반복문 탈출
        break

    sStack = [None for _ in range(len(line))] #한 줄을 한 단어씩 읽기 위해 새로운 스택 생성
    sTop = -1  #새로운 스택의 마지막 데이터를 가리키기 위한 변수, -1로 초기화 하여 비어있음을 표시

    for ch in line: #한줄의 문자열인 line에서 한 문자씩 추출하여 ch에 저장
        sTop += 1 #sTop을 1씩 늘리며 스택에 마지막으로 들어온 데이터를 가리킴
        sStack[sTop] = ch #단어 하나를 스택에 삽입

    while True:
        if sTop == -1: #스택이 텅 빈 상태면 반복문 탈출
            break
        ch = sStack[sTop] #마지막으로 들어온 데이터를 ch에 저장
        sTop -= 1 #sTop을 1씩 줄이며 마지막 입력된 값 -> 처음 입력된 값 순으로 접근
        print(ch,end="")    #문자를 출력
                            #스택은 후입선출.
        #크게 2개의 스택을 사용하고 있음.
        #문장을 담고있는 스택과 문자를 담고있는 스택으로,
        #마지막에 삽입된 문장부터 출력되는데, 그 문장에서는 문자를 거꾸로 출력.
        
    
