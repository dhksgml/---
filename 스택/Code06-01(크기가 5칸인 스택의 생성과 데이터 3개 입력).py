##stack = [None,None,None,None,None]
##top = -1
##
##top+=1
##stack[top] = "커피"
##
##top+=1
##stack[top] = "녹차"
##
##top+=1
##stack[top] = "꿀물"
##
##print("-----스택 상태-----")
##for i in range(len(stack)-1,-1,-1):
##    print(stack[i])

stack = [None,None,None,None,None]
top = -1

top += 1
stack[top] = "초코"

top += 1
stack[top] = "아이스크림 콘"

top += 1
stack[top] = "바닐라 아이스크림"

top += 1
stack[top] = "초코 아이스크림"

top += 1
stack[top] = "딸기 아이스크림"

print("------스택 상태------")
for i in range(len(stack)-1,-1,-1):
    print(stack[i])
