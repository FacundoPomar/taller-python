def PromMinMax(unalista):
	# La funcion devuelve el promedio, el minimo y el maximo de los numeros pasados como parametros
	suma = 0
	min = 99999999999
	max = -999999999999
	for num in unalista:
		if (num > max):
			max = num
		if (num < min):
			min = num
		suma += num
	
	#Devolvemos un promedio diferente a 0 si habia numeros en la lista
	if (len(unalista) > 0):
		promedio = suma/len(unalista)
	else:
		promedio = 0
	
	return (min, max, promedio)

print(PromMinMax([1, 5, 6, 2, 23, 34, 22, -8]))
