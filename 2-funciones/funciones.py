#FUNCIONES

# import turtle
#
#
# def main():
#     window = turtle.Screen()
#     dave = turtle.Turtle()
#     make_square(dave)
#
#
# def make_square(dave):
#     make_line_and_turn(dave, 100)
#
#
# def make_line_and_turn(dave, length):
#     dave.forward(length)
#     dave.left(90)
#
#
# if __name__ == '__main__':
#     main()

def calcular_dolares(cantidad):
    valor_moneda = 3.3
    return (cantidad / valor_moneda )



def run():
    print(' C A L C U L A D O R A  D E  D O L A R ES ')
    print('Convierte soles peruanos a Dolares Americanos')
    print('')

    cantidad = float(raw_input('Ingrese cantidad de soles peruanos: '))
    resultado = calcular_dolares(cantidad)

    print('S/.{} soles peruanos equivalen ${} dolares americanos' .format(cantidad, resultado))
    print('')

if  __name__ == '__main__':
    run()