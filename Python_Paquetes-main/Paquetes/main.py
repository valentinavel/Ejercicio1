from sys import path
path.append('..\\Paquetes')

def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
     
    return num
 
salir = False
opcion = 0
 
while not salir:
 
    print ("1. saber de un numero primo")
    print ("2. Operacion aritmetica")
    print ("3. Funciones")
    print ("4. Salir")
     
    print ("Elige una opcion")
 
    opcion = pedirNumeroEntero()
 
    if opcion == 1:
        print ("Opcion 1")
        import primo.primo
        print(primo.primo.es_primo(int(input("Vamos a descubrir un numero primo. Introduzca un numero:"))))
    elif opcion == 2:
        print ("Opcion 2")
        import operacion.operacion
        print("Ahora vamos hacer una operacón para esto: ")
        print(operacion.operacion.operacion(int(input("Introduzca el primer numero: ")),int(input("Introduzca el primer numero: "))))
    elif opcion == 3:
        print("Opcion 3")
        import Funciones.module
        numeros= int(input("Ahora unas funcioes de numeros, elije una: [1] pares [2] impares [3] negativos [4] positivos: "))
        if numeros == 1:
            print(Funciones.module.pares())
        elif numeros == 2:
            print(Funciones.module.impares())
        elif numeros == 3:
            print(Funciones.module.negativos())
        elif numeros == 4:
            print(Funciones.module.positivos())
        else:
            print("No es una opción valida")
    elif opcion == 4:
       salir = True
    else:
        print ("Introduce un numero entre 1 y 3")
 
print ("Fin")





