
fib_1 = 0 #0번
fib_2 = 1 #1번
fib_curr = 0
for i in range(2,3+1):
    fib_curr = fib_1 + fib_2 #2번  =  0번 + 1번
    # 3번 = 2번 + 1번
    print(f"바꾸기 전 : f(0) : {fib_1}, f(1) : {fib_2}, f(2) : {fib_curr}")
    fib_1 = fib_2
    fib_2 = fib_curr
    print(f"바꾸고 난 후 : f(1) : {fib_1}, f(2) : {fib_2}, f(2) : {fib_curr}")


