def operacion(x, y):
    tipo = input("Digite el tipo de operacion a ejecutar [suma], [resta], [multiplicacion], [division]: ")
    if tipo == "suma":
        print("suma de números")
        result = x + y
        print(result)
    if tipo == "resta":
        print("resta de números")
        result = x - y
        print(result)
    if tipo == "division":
        print("division de números")
        result = x / y
        print(result)
    if tipo == "multiplicacion":
        print("multiplicacion de números")
        result = x * y
        print(result)

