queue = [None, None, None, None, None] # 5개 짜리 None으로 가득 찬 배열 생성
front = rear = -1 # 큐가 비었다는 것을 알리기 위해 front와 rear에 -1 대입

rear += 1 # 값을 대입하기 전, 사전 작업 - 어디에 값을 대입할 지 알려줌
queue[rear] = "화사" # queue 배열의 rear에 해당하는 위치에 값 대입
rear += 1
queue[rear] = "솔라"
rear += 1
queue[rear] = "문별"

print("----- 큐 상태 -----") # 큐 상태를 보기 편하게 하기 위해 출력
print('[출구]<--',end = ' ') 
for i in range(0, len(queue), 1): # 배열 길이 만큼 반복
    print(queue[i], end = ' ')  # 큐 안에 있는 데이터 출력
print('<-- [입구]')
