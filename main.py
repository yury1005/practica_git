from calculadora import * 
global a, b

def numeros():
    global a, b
    a = int(input("Introduzca el primer número"))
    b = int(input("Introduzca el segundo número "))
    return (a, b )

option = input("""
Seleccione una operación
1. Suma 
2. Resta
3. Division
""")

try:
    option = int(option)
except:
    print ("valor no valido")

if option not in [1,2,3]:
    print ("Valor no valido")
    exit()
else:
    numeros()
    print("hola")
    if option == 1:
        suma(a,b)
    elif option == 2:
        resta(a, b)
    elif option == 3:
        if b==0:
            print("No es posible dividir entre 0")
            exit()
            
        division(a, b)

    
