def fibo(a0,a1,n):
    i = 2
    x0 = a0
    x1 = a1
    x2 = None
    print(x1)
    while i <= n:
        x2 = x0 + x1
        x0 = x1
        x1 = x2
        i = i + 1
        print(x2)
    return x2
        

x2 = fibo(0,1,10)


