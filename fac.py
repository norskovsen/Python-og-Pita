def fac(n):
    res = 1
    for i in range(1,n+1):
        res *= i
    return res

print(fac(int(input("fac> "))))
