N=int(input())



if N == 0:
    print(0)
elif N == 1:
    print(1)
else:
    fibonacci = [0] * (N + 1)
    fibonacci[0] = 0
    fibonacci[1] = 1

    def fibo(N):
        for i in range(2, N + 1):
            fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2]
        return fibonacci[N]

    print(fibo(N))
    