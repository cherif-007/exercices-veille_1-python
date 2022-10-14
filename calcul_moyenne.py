"""calcul moyenne etudiant"""
note_1 = int(input('Entrer note 1 : '))
note_2 = int(input('Entrer note 2 : '))
note_3 = int(input('Entrer note 3 : '))
moyenne = (note_1+note_2+note_3)/3
print('La moyenne des 3 notes est : {}'.format(moyenne))
if moyenne >= 16:
    print('mention : Tres bien')
elif 16 > moyenne >= 14:
    print('mention : Bien')
elif 14 > moyenne >= 12:
    print('mention : Assez-Bien')
elif 12 > moyenne >= 10:
    print('mention : Passable')
elif moyenne < 10:
    print('mention : Insufisant')
else:
    print('La moyenne est evaluee entre 0 et 20')