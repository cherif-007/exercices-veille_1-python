"""choix operateur de calcul"""
nombre_1 = int(input('Entrer nombre 1 : '))
nombre_2 = int(input('Entrer nombre 2 : '))
operateur = input('Choississez un operateur entre (+ - * /): ')
if operateur == '+':
    print('La somme des deux nombres est: {}'.format(nombre_1+nombre_2))
elif operateur == '-':
    print('La difference des deux nombres est {}'.format(nombre_1-nombre_2))
elif operateur == '*':
    print('Le produit des deux nombres est {}'.format(nombre_1*nombre_2))
elif operateur == '-':
    print('Le quotient des deux nombres est {}'.format(nombre_1/nombre_2))
else:
    print('operation echouee.!')