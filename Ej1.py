
def eliminar_duplicados_y_contar(n, identificadores):
    i = 0
    while i < n:
        j = i + 1
        while j < n:
            
            if identificadores[i] == identificadores[j]:
                identificadores.pop(j)
                n -= 1
            else:
                j += 1
        i += 1
    
   
    return n

t = int(input("Escriba el numero total de alumnos: "))


for _ in range(t):
    
    n = int(input())
    identificadores = list(map(int, input().split()))
    resultado = eliminar_duplicados_y_contar(n, identificadores)
    
   
    print(resultado)
