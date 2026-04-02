def ehPrimo(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

#main
n = int(input("digite um numero:"))
if ehPrimo(n):
    print("primo")
else:
    print("n primo")
