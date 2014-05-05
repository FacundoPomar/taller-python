:data-transition-duration: 1500
:css: style.css

-----------------------------------

.. title:: Taller de Python - Clase 2

Listas
======

Agregando Elementos
...................

Podemos agregar elementos a una lista de la forma:

.. code:: python
	
	lista = [1, 2, 3]
	lista.extend([4, 5])		# Extend agrega los elementos al final de la lista.
	lista.append(3)			# Append agrega un elemento al final de la lista.
	
También podemos trabajar con la lista, para realizar cosas como:

.. code:: python

	lista = [3, 2, 7]
	lista.sort()			#Sort ordena la lista de menor a mayor. --> [2, 3, 7]
	lista.reverse()			#invierte el orden de la lista. --> [7, 3, 2]
	
----------------------------------

:data-x: r2500

Tuplas
======

Al igual que las listas, las tuplas son estructuras de datos **Ordenadas**, **Heterogéneas** e **Indexada**. Las Tuplas se definen de la siguiente forma:

.. code::	python

	miTupla = (1, 2, 3, 4)
	
La gran diferencia con las listas, es que las tuplas una vez definidas, no pueden modificarse. Ni modificar sus valores ni modificar tu tamaño. Es por esto que se dice que las tuplas son **Inmutables**.

Podemos acceder a los datos de las tuplas, pero no podremos modificarlos. 

**¿ Por qué usarlas ?**

Las Tuplas se usan en general para setear constantes en un programa, aquellos datos que no se modificarán, pero que si se utilizarán en varias oportunidades. Por ejemplo:

.. code:: python

	negro = (0, 0, 0)
	screenResolution = (800, 600)
	
--------------------------------

:data-rotate: 90
:data-y: r1500

Sets (Conjuntos)
================

Los Sets son estructuras de datos **Heterogéneas**, **Sin Orden** y en donde no existen elementos repetidos.

Con los sets podemos realizar operaciones para:

* Saber si un elemento se encuentra en el conjunto
* Realizar las operaciones matemáticas de Unión, Intersección, Diferencia y Diferencia Simétrica.

**Declaración**

.. code:: python

	miSet = set((1, 2, 3, 4, 4))
	#O También
	miSet = set([1, 2, 3])
	#O también
	miSet = {1, 2, 3, 4, 4}

Notar que como en los Sets no existen elementos duplicados, al crearlo el 4 solo aparecerá una vez sola.
	
------------------------------------

:data-rotate: 90
:data-y: r2000

Sets
====

Operaciones
...........

.. code:: python

	miSet = set([1, 2, 3, 4])
	otroSet = set([8, 9])
	
	print (5 in miSet)		#in nos permite saber si un elemento pertenece al conjunto.
	print (miSet | otroSet)		#Unión matemática.
	print (miSet & otroSet)		#Intersección matemática.
	miCopia = otroSet.copy()		#Copiamos un set. Igual que con las listas.
	miSet.add(7)		#Agregamos un Elemento.
	miSet.discard(7)		#Eliminamos el elemento.
	
------------------------------------

:data-x: r2000

Diccionarios
============

Los Diccionarios son estructuras de pares no ordenados con el formato clave:valor.

Las Claves son únicas y estas pueden ser solo de tipos inmutables, strings y números. Tambien las tuplas pueden ser claves pero solo si no contienen objetos mutables.

Definimos un diccionario de la forma:

.. code:: python

	diccionario = {1:"Hola", 2:"Mundo", "Soy Una Clave":76, (1, 2):[1, 2]}
	
Operaciones
...........

.. code:: python

	diccionario[clave]	#Nos devuelve el valor de esa clave.
	
	#Asignamos en la clave en valor 8. Si existe, se sobre escribe. 
	# Si no, se crea la clave
	diccionario[clave] = 8	
	diccionario.keys()	#Nos devuelve todas las claves del diccionario.
	1 in diccionario.keys()	#Unimos in a keys() para saber si un elemento es una clave de un dic
	del diccionario[clave]	#Borra el elemento y su valor.
	diccionario.clear()	#Borra todo el diccionario.
	len(diccionario)	#Longitud del Diccionario
	
------------------------------------

:data-x: r2000

Diccionarios
============

Operaciones (Continuación)
..........................

Podemos unir diferentes funciones para el manejo del diccionario.

Ejemplo:

.. code:: python

	#Los diccinoarios no tienen orden, pero podemos por ejemplo, imprimir sus claves en orden
	misClaves = list(diccionario.keys())	#Obtenemos las claves y convertimos todo eso en una lista.
	misClaves.sort()		#Ordenamos los elementos
	print(misClaves)		#Imprimimos las claves del diccionario ordenadas.

---------------------------------

:data-rotate: 90
:data-y: r2000

Estructuras de Control
======================

Python cuenta con estructuras de control que nos permiten modificar el normal flujo del programa.

* If
* While
* For

---------------------------------

:data-x: r2000

Estructura Condicional If
=========================

El If nos permite evaluar un bloque booleano y actuar en consecuencia. Existen 3 variaciones:

.. code:: python

	
	if (condicion verdadera):
		Sentencia1
	
		
	if (condicion verdadera):
		Sentencia1
	else:
		#La condición no era verdadera
		Sentencia2
		
	if (condicion verdadera):
		Sentencia1
	elif (condicion verdadera):
		Sentencia2
	else:
		# Ni la primera ni la segunda condición era verdadera
		Sentencia3
		
Notar la forma de saber que se encuentra dentro de un if, es la identación de las líneas.

-------------------------------

:data-y: r2000

Bucles
======

While
.....

Los while nos permiten ejecutar bloques mientras que una condición sea verdadera.

.. code:: python

	i = 0
	
	while (i < 1000):
		print("i Todavia es menor a 1000")
		i += 1
	print("i ahora es mil")
	
-------------------------------

:data-rotate: 90
:data-x: r2000

Bucles
======

For in
......

El for nos permite iterar sobre secuencias o estructuras iterables (como las listas y las tuplas).

Su formato es:

.. code:: python

	for variable in serie_de_elementos:
		sentencia1
		..
		sentencian
		
Ejemplo:

.. code:: python

	#Iteramos por los numeros del 1 al 10
	for num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
		print(num)
		
-------------------------------

:data-x: r2000

Bucles
======

For in
......

Cuando necesitamos iterar sobre números, podemos ayudarnos de la función range() la cual genera una lista de números.

Ejemplo:

.. code:: python

	#Iteramos desde el 0 hasta el 1000
	for num in range(0, 1001):
		print(num)
		
	#seria ineficiente escribir una lista con 1000 elementos.
	
Range() también nos permite especificar un "salto".

.. code:: python

	#Imprimimos los primeros 5 numeros pares
	for num in range(0, 10, 2):
		print(num)
		
El 2 nos indica que hagamos un salto de 2 en dos. Si empezamos desde 0 imprimimos los pares, si empezamos desde el 1, imprimimos los impares. Si por ejemplo ponemos un 3, el salto sería de 3 en tres, etc..

**El for itera sobre los elementos de (en este caso) una lista. Si esos elementos fueran de otro tipo (String, Booleanos, etc) Que pasaría ?**

-------------------------------

:data-y: r2000

Break
=====

La sentencia break nos permite cortar el flujo de un bucle en cualquier momento. Por ejemplo:

.. code:: python

	i = 0
	while true:
		if (i == 100):
			break
		i += 1

El bucle termina una vez que i es igual a 100, ya que en ese caso, se ejecuta el break.

--------------------------------

:data-y: r2000

Continue
========

Parecido al break, pero en vez de cortar el bucle, hace que se salteé una "vuelta" del mismo.

Ejemplo:

.. code:: python

	#Imprimimos los números del 1 al 10000 menos los múltiplos de 9.
	i = 0
	while (i < 10000):
		if ((i % 9) == 0):
			continue
		print(i)
		i += 1
	
	
Sentencia Else en bucles
========================

Los bucles pueden contener un else al igual que un if, este else se ejecutará solo cuando en el for se agote la lista y en un while cuando la condición sea falsa.

Esto quiere decir, que el else NO se ejecutará cuando  el bucle se haya terminado a causa de un break.

-------------------------------

:data-x: r2000

Ejecutando un Programa de Python
================================

Los archivos de python son archivos de texto plano con extención .py

Si queremos escribir un programa en python, creamos un archivo de texto plano y le cambiamos la extención a .py. 

Para ejecutarlo, podemos o hacerle doble clic o ejecutarlo desde consola de la forma:

.. code:: bash

	python3 nombre_del_archivo.py
	
O si utilizamos Geany, haciendo click en f5.
