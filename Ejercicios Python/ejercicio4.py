# Mayor de tres números: 
# Crea una función que tome tres números como argumentos y devuelva el mayor de ellos.

def mayor(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        print('El mayor es: ', num1)
    elif num2 > num3 and num2 > num1:
        print('El mayor es: ', num2)
    else:
        print('El mayor es: ', num3)

mayor(6, 2, 8) # Mayor 7
mayor(5, 10, 1) # Mayor 10
mayor(6, 1, 9) # Mayor 9