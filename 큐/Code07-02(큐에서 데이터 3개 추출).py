queue = ["화사", "솔라", "문별", None, None]
front = -1
rear = 2

print("----- 큐 상태 -----")
print('[출구] <--', end = ' ')
for i in range(0, len(queue), 1):
    print(queue[i], end = ' ')
print('<-- [입구]')
print("------------------")

# 실질적으로 삭제를 진행하는 부분
front += 1 # 앞에서 1칸 증가
data = queue[front] # front 위치에 데이터 기억
queue[front] = None # front 위치에 None 저장
print('deQueue -->', data) # 기억한 값 출력

front += 1
data = queue[front]
queue[front] = None
print('deQueue -->', data)

front += 1
data = queue[front]
queue[front] = None
print('deQueue -->', data)
print("-------------")

print("----- 큐 상태 -----")
print("[출구] <--", end = ' ')
for i in range(0, len(queue), 1):
    print(queue[i], end = ' ')
print('<-- [입구]')

