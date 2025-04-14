
direction = input("방향을 입력하세요(left, right, up, down): ")

left = 'left'
right = 'right'
up = 'up'
down = 'down'

if direction in left:
    print("왼쪽으로 이동합니다.")

elif direction in right:
    print("오른쪽으로 이동합니다.") 
    
elif direction in up:
    print("위로 이동합니다.")
    
elif direction in down:
    print("아래로 이동합니다.")           
    
else:
    print("알 수 없는 명령입니다.")    