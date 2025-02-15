from itertools import permutations

N = int(input())
A = list(map(int, input().split()))
operator = list(map(int, input().split())) 

# 가능한 연산자 경우의수
def operator_placement(operator):
    operator_list = []
    operator_list.extend(['+'] * operator[0])
    operator_list.extend(['-'] * operator[1])
    operator_list.extend(['*'] * operator[2])
    operator_list.extend(['/'] * operator[3])  

    return list(set(permutations(operator_list, len(operator_list))))

# 연산 수행
def calculate_numbers(A, operator_permut):
    result = A[0]
    
    for i in range(N - 1):  
        next_number = A[i + 1]
        operator = operator_permut[i] 
        
        if operator == '+':
            result += next_number
        elif operator == '-':
            result -= next_number
        elif operator == '*':
            result *= next_number
        elif operator == '/':  
            if result < 0:
                result = -(-result // next_number)  # 음수 나눗셈 처리
            else:
                result //= next_number

    return result


operator_cases = operator_placement(operator)
#출력값들 비교하기기
max_value = float('-inf')
min_value = float('inf')

for op_permut in operator_cases:
    res = calculate_numbers(A, op_permut)
    max_value = max(max_value, res)
    min_value = min(min_value, res)

print(max_value)
print(min_value)
