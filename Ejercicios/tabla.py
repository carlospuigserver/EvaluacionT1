def tabla():
    arg=int(input("Escribe un número entre el 1 y el 9:  "))
    arg2=int(input("Escribe un número entre el 1 y el 9: "))
    if arg<1 or arg>9 or arg2<1 or arg2>9:
        print("Error")
    for i in range(arg):
        print()
        for j in range(arg2):
           print('*',end="\t")
    print()

tabla()