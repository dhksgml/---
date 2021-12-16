
#스택이 꽉 찼는지 확인하는 함수
def isStackFull():
    global SIZE,stack,top
    if(top == SIZE-1):
        return True
    else:
        return False

#스택이 비었는지 확인하는 함수
def isStackEmpty():
    global SIZE,stack,top
    if (top == -1):
        return True
    else:
        return False

#스택에 data 추가하는 함수
def push(data):
    global SIZE,stack,top
    if(isStackFull()):
        return None
    top += 1
    stack[top] = data

#스택에서 삭제,반환하는 함수
def pop():
    global SIZE,stack,top
    if(isStackEmpty()):
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

#스택의 top 값을 확인하는 함수
def peek():
    global SIZE,stack,top
    if(isStackEmpty()):
        print("스택이 비었습니다.")
        return None
    return stack[top]

#떨어뜨릴 돌의 개수를 입력 받습니다.
SIZE = int(input("떨어뜨릴 돌의 갯수를 입력하세요 ==> "))

#스택을 None으로, top은 -1로 초기화
stack = [None for _ in range(SIZE)]
top = -1

# "n번째 돌" 이라는 값을 스택에 추가하기 위해 선언한 변수
i = 1
print()
print("과자 집 가는 길")

#스택이 다 찰 때까지 data를 추가하며 출력
while True:
    push(str(i)+"번째 돌")
    if(isStackFull()):
        print(peek())
        break
    print(peek(),end="-->")
    i+=1
print()
print()


print("집에 돌아오는 길")
#스택이 빌 때까지 삭제하며 출력
while True:
    out = pop()
    if(isStackEmpty()):
        print(out)
        break
    else:
        print(out,end="-->")
print()
    
