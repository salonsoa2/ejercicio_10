
import stats_data as sd
list = list()

while True:
    lista = float(input("escribe varios numeros: "))
    if lista == "fin":
        break
    list.append(lista)

lista_numeros = sd.StatsData(list)
print("lista numeros:", lista_numeros.l_data)
print("Media:", lista_numeros.mean)
print("Mediana:", lista_numeros.median)
print("Varianza:", lista_numeros.variance)
