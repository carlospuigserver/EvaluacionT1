
def sumar(a,b,c):
    return a+b+c

def main():
    matriz = []
    for i in range(3):
        fila = []
        for j in range(3):
            fila.append(int(input("Ingrese un numero: ")))
        fila.append(sumar(fila[0],fila[1],fila[2]))
        matriz.append(fila)
    print(matriz)

main()

#sumas incorrectas

def main():
    matriz = []
    for i in range(3):
        fila = []
        for j in range(3):
            fila.append(int(input("Ingrese un numero: ")))
        matriz.append(fila)
    for i in range(3):
        for j in range(3):
            if i == j:
                matriz[i][j] = 0
    print(matriz)
