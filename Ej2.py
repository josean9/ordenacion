peso = int(input("Escriba el peso maximo por gondola: "))
n = int(input("Escriba el numero de niños: "))

niños = list(map(int, input("Escribe el peso de los niños: ").split()))

niños.sort()
contador = 0
while True:
    
    try:
        if peso > niños[contador]+niños[contador+1]:
            niños[contador] += niños[contador+1]
            niños.pop(contador+1)
        elif peso <= niños[contador]:
            contador += 1
        else:
            print(niños)
            break
    except IndexError:
        break
print(len(niños))
    