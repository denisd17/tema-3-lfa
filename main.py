from copy import deepcopy
'''
INPUT:

NR STARI
STARI FINALE
(S1) (S2) (CARACTER) (VARF STIVA) (NOU VARF AL STIVEI)
 .
 .
 .
 '''
#nu se trec intre paranteze rotunde, dar se pune spatiu intre ele
#Z e caracterul de inceput al stivei
# # este lambda

#UTILIZAT PENTRU A RETINE UN ISTORIC AL TRANZITIILOR EFECTUATE (SAU VERIFICATE)
def generareTranz(cuvant, stare1, stare2, stiva, tranz):
    tranzitie = cuvant +" "+ str(stare1) +" "+ str(stare2) + " "
    for c in stiva:
        tranzitie = tranzitie + c
    tranzitie = tranzitie + " " + tranz[0] + " " + tranz[1] + " " + tranz[2]
    return tranzitie

#APD - PARCURGERE IN ADANCIME
def APD(cuvant, stare, stack):

    #VERIFICARE CUVANT VID, STARE FINALA SI STIVA VIDA
    if stare in stari_finale and cuvant == "":
        if len(stiva) == 0 or (len(stiva) == 1 and stiva[0] == 'Z'):
            print("ACCEPTAT")
            exit()

    #VERIFICARE CUVANT VID INCA NEACCEPTAT (CAUTARE DE LAMBDA TRANZITII)
    elif cuvant=="":
        for i in range(0, nr_stari):
            if len(A[stare][i]) != 0:
                for j in range(len(A[stare][i])):
                    tranzitie = generareTranz(cuvant, stare, i, stack, A[stare][i][j])
                    if tranzitie not in tranzitii:
                        tranzitii.append(tranzitie)
                        tranz = A[stare][i][j]
                        if tranz[0] == '#':
                            if stack[-1] == tranz[1]:
                                copie_stiva = deepcopy(stack)
                                copie_stiva.pop()
                                if tranz[2] != '#':
                                    for c in tranz[2][::-1]:
                                        copie_stiva.append(c)
                                APD(cuvant, i, copie_stiva)

    #VERIFICARE CUVANT
    else:
        for i in range(0, nr_stari):
            if len(A[stare][i]) != 0:
                for j in range(len(A[stare][i])):
                    tranzitie = generareTranz(cuvant, stare, i, stack, A[stare][i][j])
                    if tranzitie not in tranzitii:
                        tranzitii.append(tranzitie)
                        tranz = A[stare][i][j]
                        if tranz[0] == cuvant[0] or tranz[0] == '#':
                            if stack[-1] == tranz[1]:
                                copie_stiva = deepcopy(stack)
                                copie_stiva.pop()
                                if tranz[2] != '#':
                                    for c in tranz[2][::-1]:
                                        copie_stiva.append(c)
                                if tranz[0] == '#':
                                    APD(cuvant, i, copie_stiva)
                                else:
                                    APD(cuvant[1:], i, copie_stiva)




#CITIRE DATE
f = open("input.txt","r")

nr_stari = int(f.readline())
A = [[[] for i in range(nr_stari)]for j in range(nr_stari)]
stari_finale = [int(x) for x in f.readline().split()]
for line in f:
    s = int(line[0])
    d = int(line[2])
    tranzitie = line[4:].split()
    A[s][d].append(tranzitie)

stiva = ['Z']
tranzitii = []

cuvant = input("Introduceti cuvantul: ")
APD(cuvant, 0, stiva)
print("NEACCEPTAT")

