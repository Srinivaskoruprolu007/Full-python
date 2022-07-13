def factorial(n):
    if n==1:
        return 2
    f = n*factorial(n-1)
    return f


print(factorial(5))