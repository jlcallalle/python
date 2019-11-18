'''OPERADORES MATEMÁTICOS'''


# this is the first comment
spam = 1  # and this is the second comment
text = "# This is not a comment because it's inside quotes."

suma = 2+2
print(suma)

resta = 5-3
print(resta)

multiplica = 3 * 4
print(multiplica)

division = 5 / 4
print(division)

division2 = 5.0 / 4.0
print(division2)

residuo = 10 % 2
print(residuo)

potencia = 3 ** 2
print(potencia)

mayor = 5 > 3
print(mayor)

igual = 10 == 10

noigual = 10 == 9
print(noigual)


''' VALORES Y TIPOS '''

# 'Integer
print(type(2))

# 'Float
print(type(2.0))

# 'float'
print(type(2.3))

# String
print(type('jorge'))

# 'Bolean
print (type(3==4)) 

# Integer
print(type(2+3))



# Concatenar
print('hola' + 'hola')

print('curso' * 3)

# calculo
print(3.14159 * 3**2)

pi = 3.14159
radio = 3
area = pi * radio**2
print(area)


# Listas las declaras con corchetes. Estas pueden tener una lista dentro o cualquier tipo de dato
L = [22, True, 'una lista', [1, 2]]  

L[0]
22

#Tuplas se declaran con paréntesis, recuerda que no puedes editar los datos de una tupla después de que la has creado.

T = (22, True, 'una tupla', (1, 2)) 
>>> T[0] 
 22

# Diccionarios, En los diccionarios tienes un grupo de datos con un formato: la primera cadena o número será la clave para acceder al segundo dato, el segundo dato será el dato al cual accederás con la llave. Recuerda que los diccionarios son listas de llave:valor.
D = {"Kill Bill": "Tamarino", "Amelie": "Jean-Pierre Jeunet"} 
D["Kill Bill"]
 "Tamarino"


 https://platzi.com/clases/1104-python/7166-guia-de-instalacion-y-conceptos-basicos/