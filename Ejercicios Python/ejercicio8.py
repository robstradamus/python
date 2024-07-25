# Factorial de un número: 
# Escribe una función que calcule el factorial de un número dado (por ejemplo, factorial(5) = 5 * 4 * 3 * 2 * 1).

def factorial(num):
    if num == 1:
        return 1
    elif num == 0:
        return 0
    else:
        for x in range(1,num):
            num *= x
            print(num,'x',x,'=',num)

print(factorial(1))
print(factorial(0))
factorial(5)