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

Los Módulos y Funciones nos permiten extraer código de nuestro programa principal para (en lo posible) volverlo genérico y de esta forma, poder utilizarlo muchas veces sin tener que copiar código.

Formato de una función:

.. code:: python

	def nombreDeLaFuncion (parametros):
		sentencia 1
		sentencia 2
		...
		sentencia N
		
Notar que al igual que con las estructuras de control, definimos que se encuentra dentro de la función utilizando la indentación. *def* es la palabra clave que nos indica que esto es una función.
		
-------------------------------------------

:data-x: r2000

Funciones
=========

La sentencia *return* nos permite que la función retorne un valor procesado si es que así lo necesitamos.

Los parámetros nos permiten enviarle datos a las funciones para que estas puedan utilizarlos. Ejemplo:

.. code:: python

	def Cubo(x):
		return x**3
		
La función Cubo() en este caso, nos devolverá el valor que le pasemos como parámetro, elevado al cubo. **¿ Cómo lo utilizamos ?**

.. code:: python

	a = 3
	resultado = Cubo(a)
	print(resultado)
	
--------------------------------------------

:data-rotate: 90


Funciones
=========

Como parámetro envié la variable *a*, pero en la declaración nombré al parámetro x.

Esto funciona ya que la correlación de parámetros en python es a través de la posición de los mismos.

.. code:: python

	def Mayor(a, b):
		if (a > b):
			return a
		return b
		
	a = 15
	b = 34
	resultado = Mayor(b, a)
	print(resultado)
	
**¿Qué imprime?**

----------------------------------------------

:data-y: r2000

Funciones
=========

Las funciones siempre devuelven algo, aún si no indicamos un *return*.

.. code:: python
	
	def MiNombre(nombre):
		print(nombre)
		
	print(MiNombre("Facundo"))
	
Los parámetros siempre son copias de los datos (Osea, son parámetros pasados por valor).

.. code:: python

	def Reducir(x):
		x -= 1
	
	x = 10
	reducir(x)
	print(X)
	
Esto pasa con todos los tipos de datos vistos ? Probemos con Strings, Enteros, Flotantes, Listas...

--------------------------------------------

:data-y: r2000

Funciones
=========

Si paso como parámetro una lista y la modifico, el cambio si se verá reflejado en el programa principal. 

**¿Cómo lo Evitamos?**

Como se había mencionado, *return* devuelve un solo valor. Si queremos que nuestra función devuelva más de un solo valor, tenemos que utilizar alguna estructura de datos.

.. code:: python

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
	
-------------------------------------

:data-rotate: 90

Funciones
=========

Existen ocaciones en donde podemos tener parámetros que no sean obligatorios, osea opcionales. 

La forma de manejar esto en python es a través de parámetros por defecto.

.. code:: python

	def Saludo(nombre, saludo = "Hola"):
		print(saludo + " " + nombre)
		
	Saludo("Facundo")
	Saludo("Facundo", "Chau")
	Saludo("Facundo", "Que tal")
	
Los parámetros por defecto nos permiten definir funciones con una cantidad de parámetros variantes. **Tener en cuenta:** Los parámetros por defecto siempre van al final de la lista de parámetros. **Uso incorrecto**

.. code:: python

	def Saludo(saludo = "Hola", nombre):
		print(saludo + " " + nombre)

	#SyntaxError: non-default argument follows default argument

--------------------------------------

:data-y: r2000

Funciones
=========

Variables Globales y Locales
............................

Las variables definidas en el programa principal, serán globales a todo el programa (incluida las funciones). Mientras que las variables definidas en las funciones, serán locales a esa misma función.

Es una mala práctica de programación utilizar variables globales en nuestros programas. Para ello existen los parámetros.

**Funciones Dentro de Funciones**

Es posible declarar funciones dentro de una función, y al igual que las variables, esta función será local a la función en donde es declarada.
