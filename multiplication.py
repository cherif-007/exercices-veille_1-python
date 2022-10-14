"""Demande nombre et affiche table de multiplication"""
nombre = int(input('Entrer un nombre: '))
for i in range(0,11):
    print(' {0} x {1} = {2}'.format(nombre, i, nombre*i))
    i += 1