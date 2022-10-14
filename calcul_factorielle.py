"""calcul factorielle"""
nombre = int(input('Entrer nombre: '))
fact = 1
if nombre == 0:
    print('La factorielle de 0 est 1')
elif nombre < 0:
    print('veuillez saisir un nombre positif non nul.!')
else:
    for i in range(2, nombre+1):
        fact = fact * i
    print('La factorielle de {}! est: {}'.format(nombre, fact))