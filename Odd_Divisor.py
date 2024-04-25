#se pide el numero de casos que se van a ingresar
num = int(input())
#por cada caso se pide un numero para comprobar si tiene algun numero divisor impar 
for n in range(num):
    k = int(input())
#el numero k entrara dentro del while siempre que tenga divisores pares
    while k % 2 == 0:
        k = k // 2
#comprovamos si k = 1 porque esto quiere decir que solo tiene divisores pares, de otra manera usamos el else cuando k es diferente de 1 y deja de entrar al while, lo que nos dice que k tiene algun divisor impar
    if k == 1:
        print("NO")
    else:
        print("YES")
