from testMy import *
from archivio import *

def controllo():
    #contiamo i test falliti
    testFalliti=0
    print("==========> Inizio nuovo test <=============\n\n")
    # creo l'archivio
    # archivio = Archivio()

    ## Checkvoto
    print("-----------------test checkvoto----------------")
    testFalliti += testEqual((checkvoto(18)), True)
    testFalliti += testEqual((checkvoto(22)), True)
    testFalliti += testEqual((checkvoto(33)), False)
    testFalliti += testEqual((checkvoto("r")), False) 
    testFalliti += testEqual((checkvoto(str(18))), False)
    testFalliti += testEqual((checkvoto(str(16))), False)
    testFalliti += testEqual((checkvoto(12)), False)

    print("-----------------test exists in tup list----------------")

    lista = [("AB", 5), ("CD", 6)]
    testFalliti += testEqual((exists_in_tup_list(lista, 5, 1)), True)
    testFalliti += testEqual((exists_in_tup_list(lista, "AB", 0)), True)
    testFalliti += testEqual((exists_in_tup_list(lista, "CD", 0)), True)
    testFalliti += testEqual((exists_in_tup_list(lista, 6, 0)), False)

    print("-----------------test exists in----------------")

    dict = {1:"Mario", 2:"Luca", 3:"John"}
    testFalliti += testEqual(exists_in(dict, 5), False)
    testFalliti += testEqual(exists_in(dict, 2), True)
    testFalliti += testEqual(exists_in(dict, 3), True)
    testFalliti += testEqual(exists_in(dict, 4), False)


    # abbiamo finito ?
    if testFalliti == 0:
        print("\t****Test completati -- passare ai test in main.py")
    else:
        print("Test falliti: ", testFalliti)

# eseguo i test automatici
controllo()

"""  other test
# test base su studente
    print("==========> Test 1")
    #
    
    try:
        stud1 = Studente("Rossi", "Carlo", 345655)
        print("Pass")
    except:
        testFalliti += 1
        print("Errore nella creazione di uno studente")
        exit(1)
    
    testFalliti += testEqual(stud1.get_cognome(), "Rossi")
    testFalliti += testEqual(stud1.get_nome(), "Carlo")
    stud1.set_nome("Mario")
    testFalliti += testEqual(stud1.get_nome(), "Mario")
    testFalliti += testEqual(stud1.get_matricola(), 345655)
    testFalliti += testEqual(stud1.get_listaesami(), [])
    testFalliti += testEqual(str(stud1), "Mario Rossi mat: 345655 esami: no")
    testFalliti += testEqual(stud1.get_voto("544MM"), None)
    testFalliti += testEqual(stud1, Studente("Rossi", "Mario", 345655))
    testFalliti += testEqual(stud1.media(), None)
    stud2 = Studente("Bianchi", "Luigi", 528611)
    testFalliti += testEqual(stud1 == stud2, False)

    
    # test voti studente
    print("==========> Test 2")
    #
    testFalliti += testEqual(stud1.registra_esame("544MM", 23),True)
    testFalliti += testEqual(stud1.registra_esame("564GG", 21),True)
    testFalliti += testEqual(stud1.get_voto("544MM"), 23)
    testFalliti += testEqual(stud1.get_voto("564GG"), 21)
    testFalliti += testEqual(stud1.get_voto("456FF"), None)
    testFalliti += testEqual(stud1.get_listaesami(), [("544MM", 23), ("564GG", 21)])
    testFalliti += testEqual(str(stud1), "Mario Rossi mat: 345655 esami: [('544MM', 23), ('564GG', 21)]")
    testFalliti += testEqual(stud1, Studente("Rossi", "Mario", 345655))
    testFalliti += testEqual(stud1.modifica_voto("564GG", 19),True)
    testFalliti += testEqual(stud1.get_voto("564GG"), 19)
    testFalliti += testEqual(stud1.get_listaesami(), [("544MM", 23), ("564GG", 19)])
    testFalliti += testEqual(stud1.media(), 21.0)
    testFalliti += testEqual(stud1.cancella_esame("564GG"),True)
    testFalliti += testEqual(stud1.get_listaesami(), [("544MM", 23)])
    testFalliti += testEqual(stud1.media(), 23.0)
    stud1.set_listaesami([])
    testFalliti += testEqual(stud1.get_listaesami(), [])
    stud1.set_listaesami([("544MM", 23), ("564GG", 21)])
    testFalliti += testEqual(stud1.get_listaesami(), [("544MM", 23), ("564GG", 21)])
    testFalliti += testEqual(stud1.media(), 22.0)
    # test valori errati studente
    print("==========> Test 3")
    #
    try :
        Studente("Lucato", "Giusi", -2)
        testFalliti += 1
    except(ValueError):
        print("Pass")
    try :
        stud1.set_listaesami([("ABV23", 42)])
        testFalliti += 1
    except(ValueError):
        print("Pass")
    try:
       stud1.set_listaesami([("ABV23", 12)])
       testFalliti += 1
    except(ValueError):
        print("Pass")
    try:
        stud1.set_listaesami([("ABV23", 12)])
        testFalliti += 1
    except(ValueError):
        print("Pass")
    try:
        Studente("Lucato", 2, 345655)
        testFalliti += 1
    except(TypeError):
        print("Pass")
    try:
        Studente(1, "Giusi", 345655)
        testFalliti += 1
    except(TypeError):
        print("Pass")
    try:
        stud2.set_nome(2)
        testFalliti += 1
    except(TypeError):
        print("Pass")
    try:
        stud2.set_cognome(2)
        testFalliti += 1
    except(TypeError):
        print("Pass")
    try:
        stud2.set_matricola("345655")
        testFalliti += 1
    except(TypeError):
        print("Pass")
    try:
        stud1.set_listaesami([(2345, 23)])
        testFalliti += 1
    except(TypeError):
        print("Pass")
    try:
        stud1.set_listaesami([("2345", "a2")])
        testFalliti += 1
    except(TypeError):
        print("Pass")

    
    testFalliti += testEqual(stud1.registra_esame("144MM", 15), False)
    testFalliti += testEqual(stud1.registra_esame("144MM", 35), False)
    testFalliti += testEqual(stud1.registra_esame("144MM", 25), True)
    testFalliti += testEqual(stud1.registra_esame("144MM", 30), False)
    testFalliti += testEqual(stud1.registra_esame("456FF", "15"), False)
    testFalliti += testEqual(stud1.registra_esame(456, 15), False)
    testFalliti += testEqual(stud1.modifica_voto("fdewad", 15), False)
    testFalliti += testEqual(stud1.modifica_voto("144MM", "15"), False)
    testFalliti += testEqual(stud1.modifica_voto(456, 15), False)
    testFalliti += testEqual(stud1.cancella_esame("fdewad"), False)
    testFalliti += testEqual(stud1.cancella_esame(456), False)
    testFalliti += testEqual(stud2.media(), None)

"""