#coding=utf-8
import time
import numpy as np

titre=input(' Vous voulez faire un random de quoi?? \n')
if(titre != ''):
    print ('\t +++Random pour \" ' +titre+ ' \" because you are trop flemmard +++\n')
else:
    print ('\t +++Random pour anything what you do ou you don\'t do koa mety +++\n')

print(' génération de la liste \n')
choix = []

while True:
    element = input(" valeur : ")
    
    if element == '':
        break
    else:
        choix.append(element)
    
        print (choix)
def mine():
    i = int(input('Choisissez le nombre d\'élément  nécessaire : \n\n'))

    while(i != 0):
            print("\t+++ Random generation +++\n")
            resultat = np.random.choice(choix)
            i=i-1

            print(resultat)        
while True:
            loop = input('faire une génération ??(Y or N) ')
            if ( loop == 'Y'):
                mine()
            else:
                print(" Bye ")
                time.sleep(5)
                break
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       