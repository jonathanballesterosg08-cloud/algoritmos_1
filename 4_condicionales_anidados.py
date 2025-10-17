nota = float(input("ingrese su nota"))

if nota >= 0 and nota <= 2.9:
    print('deficiente')
elif nota >= 3 and nota <= 3.9:
    print('bueno')
else:
    print('excelente')


numero_1 = int(input('ingrese su numero'))
numero_2 = int(input('ingrese su numero'))
numero_3 = int(input('ingrese su numero'))

if numero_1 > numero_2 and numero_2 > numero_3:
    print('numero 1 es mayor')
elif numero_2 > numero_1 and numero_2 > numero_3:
    print('numero 2 es mayor')
else:
    print('numero 3 es mayor')




