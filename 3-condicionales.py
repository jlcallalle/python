#CONDICIONALES

print('a' == 'a')
print('david' == 'David')
print('z' > 'a')

print(10 != 10)
print(15 != 10)

# AND
print(10 > 15 and 15 > 20)
print('a' == 'a' and 'b' == 'b')
print (True and True)

# OR
print('a' == 'a' or 'b' != 'b')
print(False or False)

#operadores relacoinales compara y devuelven
#operaciones boleanas

def say_hello(age):
    if age > 18:
        print('es mayor')
    else:
        print('es menor de edad')
