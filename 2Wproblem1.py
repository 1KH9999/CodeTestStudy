def find_ball_position(moves, swap_list):
    
    cups = [1, 0, 0]

   
    for x, y in swap_list:
        cups[x-1], cups[y-1] = cups[y-1], cups[x-1]

   
    for i in range(3):
        if cups[i] == 1:
            return i + 1  

    return -1  
M = int(input())
swap_list = [tuple(map(int, input().split())) for _ in range(M)]

print(find_ball_position(M, swap_list))
