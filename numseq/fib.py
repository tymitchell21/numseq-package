def fib(n):
    if n == 1: 
        return 1
    result = 0
    num = 0
    nextNum = 1
    for i in range(1,n):
        result = num + nextNum
        num = nextNum
        nextNum = result
    return result