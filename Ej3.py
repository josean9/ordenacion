n = int(input("numero de pelis: "))
horarios = []
total = 0

for _ in range(n):
    ini , fin = map(int, input().split())
    horarios.append([ini,fin])



for inicio, fin in horarios:
    
    if inicio >= tiempo_actual:
        tiempo_actual = fin  
        peliculas_vistas += 1  


print("Número máximo de películas que puedes ver:", peliculas_vistas)