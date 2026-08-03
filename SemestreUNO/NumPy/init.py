import numpy as np 

# diferencia d elista y array

lista = [1, 2, 3, 4, 5] # Consta de elementos pertenecientes a distintos tipos de datos

array = np.array([1, 2, 3, 4, 5]) # Consta de elementos pertenecientes a un mismo tipo de datos 
# la "i" indica que el tipo de dato es entero (integer)
# con la letra "d" se indica que el tipo de dato es doble precisión (double)

# Para aplicar operaiones alegráicas necesitamos un array, que el mismo tiene que tener dentro del vector, un mismo tipo de dato, para que se pueda aplicar la operación.



# Matriz

matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # No es posible crear una matriz con el módulo array, ya que este solo permite crear arrays unidimensionales. 

for fila in matriz:
    print(fila)


    