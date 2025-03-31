##def fontion (n):
##    nbr0 = 0
##    nbr1 = 1
##    nbr2 = 0
##    
##    for i in range(n-2):
##        nbr2 = nbr1 + nbr0
##        nbr0 = nbr1
####        nbr1=nbr2
####        
####    return nbr2
####print (fontion(50))
##
##


##operation=''
##
##nombre1 =''
##
##nombre2=''
##
##rep=0
##
##calcule = input('ecrire le calcul')
##
##
##
##for i in range(len(calcule)):
##
##    if calcule[0]== '-':
##
##        nombre1='-'
##
##
##
##    if calcule[i]== '+' or calcule[i]=='-' or calcule[i]=='/' or calcule[i]=='*' and i != 0:
##
##        operation = calcule[i]
##
##
##
##    if operation == '':
##
##        nombre1 = calcule[i]
##
##
##
##    else:
##
##        nombre2 = calcule[i]
##
##
##
##nombre1 = int(nombre1) 
##
##nombre2= int(nombre2)
##
##
##
##if operation == '+' :
##
##    rep = nombre1 + nombre2
##
##
##
##if operation == '-':
##
##    rep = nombre1-nombre2
##
##
##
##if operation== '/':
##
##    if nombre2 != 0:
##
##        rep = nombre1 / nombre2
##
##    else : print('impossible change de nrb gogole')
##
##
##
##if operation == '*':
##
##    rep= nombre1 * nombre2
##
##
##
##print(rep)

##def pendu():
##    mot = 'bateau'
##    guess=['_'] * len(mot)
##    nbess=0
##    while '_' in guess:
##     l=input('entrez lettre  ')
##     nbess= 1+nbess
##     for indese in range(len(mot)):
##        if mot[indese] ==l:
##           guess[indese]=l 
##           print(guess)
##    return nbess
##
##print(pendu())


def match_pattern(cle, texte):
    for i in range(len(texte)):
        rep = True
        for j in range(len(cle)):
            if(i+j) >= len(texte):
                rep= False
            elif cle[j]!= texte[i+j]:
                rep= False
        if rep :
            list_rep.append(i)

    return list_rep.append
            
                    


print (match_pattern('AB', 'AABBBRECTAABCFTAAB'))