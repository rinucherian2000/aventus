def fib(n):
    a,b,c= 0,1,1
    res=1
    if n == 1:
        print(a)
    else:
        print(a)
        print(c)

    while (c < n):
        c = a + b
        res = res + 1
        a,b=b,c
        print(c)

    return res

result = fib(21)
print("index of the fibonacci series is :",result)

