:data-transition-duration: 1500
:css: style.css

-----------------------------------

.. title:: Taller de Python - Clase 2

Estructuras de Control (Repaso)
...............................

**Condicionales:**

.. code:: python

	a = 2
	b = 3
	if (a > b):
		print("A es mayor a B")
	else:
		print("B es mayor a A")
		
**Bucles:**

.. code:: python

	#Imprimimos los 10 primeros numeros enteros positivos
	
	#Con un for
	for num in range(1, 11):
		print(num)
		
	#Con un while
	i = 1
	while (i <= 10):
		print(i)
		i += 1
		
**Finalización de los bucles:**

En el for, es por agotamiento de la lista o estructura sobre la cual itera.

En el While, es cuando su condición pasa a ser falsa.

--------------------------------------------

:data-y: r1500
:data-rotate: 180

Clase 3 - Modulos y Funciones
=============================

Los Módulos y Funciones nos permiten 
