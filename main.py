# Script di test Assegnamento 1py 622AA 2023/24 (non modificare)
from testMy import *
from archivio import *

def controllo():
    #contiamo i test falliti
    testFalliti=0
    print("==========> Inizio nuovo test <=============\n\n")
    # creo l'archivio
    archivio = Archivio()

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
    testFalliti += testEqual(stud1.registra_esame("456FF", "15"), False)
    testFalliti += testEqual(stud1.registra_esame(456, 15), False)
    testFalliti += testEqual(stud1.modifica_voto("fdewad", 15), False)
    testFalliti += testEqual(stud1.modifica_voto("144MM", "15"), False)
    testFalliti += testEqual(stud1.modifica_voto(456, 15), False)
    testFalliti += testEqual(stud1.cancella_esame("fdewad"), False)
    testFalliti += testEqual(stud1.cancella_esame(456), False)
    testFalliti += testEqual(stud2.media(), None)

    # archivio: inserimenti, elimina e note corretti e sbagliati
    print("==========> Test 4")
    #
    testFalliti += testEqual(archivio.get_studenti(), [])
    testFalliti += testEqual(archivio.inserisci(stud1, ""), True)
    testFalliti += testEqual(archivio.get_studenti(), [345655])
    testFalliti += testEqual(str(archivio), "Mario Rossi mat: 345655 esami: [('544MM', 23), ('564GG', 21)]\n")
    testFalliti += testEqual(archivio.inserisci(stud2, 55), False)
    testFalliti += testEqual(archivio.inserisci(stud2), True)
    testFalliti += testEqual(archivio.get_studenti(), [345655, 528611])
    testFalliti += testEqual(str(archivio), "Mario Rossi mat: 345655 esami: [('544MM', 23), ('564GG', 21)]\nLuigi Bianchi mat: 528611 esami: no\n")
    stud3 = Studente("Rossi", "Maria", 345654)
    stud4 = Studente("Piazza", "Lucia", 232526)
    testFalliti += testEqual(archivio.inserisci(stud3,"gemella"), True)
    testFalliti += testEqual(archivio.inserisci(stud4), True)
    testFalliti += testEqual(archivio.inserisci(Studente("Verdi", "Rossana", 345655), ""), False)
    testFalliti += testEqual(stud1, archivio.studente(345655))
    testFalliti += testEqual(archivio.studente(345654), stud3)
    testFalliti += testEqual(archivio.studente(345656), None)
    testFalliti += testEqual(archivio.elimina(345654), True)
    testFalliti += testEqual(archivio.studente(345654), None)
    testFalliti += testEqual(archivio.get_note(345655), "")
    testFalliti += testEqual(archivio.get_note(345653), None)
    testFalliti += testEqual(archivio.modifica_note(345655, "note"), True)
    testFalliti += testEqual(archivio.get_note(345655), "note")
    testFalliti += testEqual(archivio.inserisci(stud3), True)

    # test su registra_esame
    print("==========> Test 5")
    testFalliti += testEqual(archivio.registra_esame(345654, "444GG", 27), True)
    testFalliti += testEqual(archivio.registra_esame(345654, "564GG", 18), True)
    testFalliti += testEqual(archivio.registra_esame(528611, "564GG", 18), True)
    testFalliti += testEqual(archivio.registra_esame(444655, "564GG", 18), False)  # matricola non presente
    
# test su media
    print("==========> Test 6")
    testFalliti += testEqual(archivio.media(111111), None)
    testFalliti += testEqual(archivio.media(345655), 22.0)

#test su modifica voto
    print("==========> Test 7")
    testFalliti += testEqual(archivio.modifica_voto(345654, "444GG", 30),True)
    testFalliti += testEqual(archivio.modifica_voto(345654, "564GG", 20),True)
    testFalliti += testEqual(archivio.modifica_voto(345654, "456FF", 18),False) #matricola non presente
    testFalliti += testEqual(archivio.media(345654),25)

#test su conta studenti promossi
    print("==========> Test 8")
    testFalliti += testEqual(archivio.conta_studenti_promossi("564GG"),3)
    testFalliti += testEqual(archivio.conta_studenti_promossi("564GG",21),1)
    testFalliti += testEqual(archivio.conta_studenti_promossi("564GG",25),0)

#test su lista studenti promossi
    print("==========> Test 9")
    testFalliti += testEqual(archivio.conta_studenti_promossi("564GG"), len(archivio.lista_studenti_promossi("564GG")))
    testFalliti += testEqual(archivio.conta_studenti_promossi("564GG", 21),len(archivio.lista_studenti_promossi("564GG", 21)))
    testFalliti += testEqual(archivio.conta_studenti_promossi("564GG", 25), len(archivio.lista_studenti_promossi("564GG", 25)))

# test su lista_media
    print("==========> Test 10")
    testFalliti += testEqual(len(archivio.lista_studenti_media()), 3)
    testFalliti += testEqual(len(archivio.lista_studenti_media(22)), 2)
    testFalliti += testEqual(len(archivio.lista_studenti_media(25)), 1)

# test su cancella esame
    print("==========> Test 11")
    testFalliti += testEqual(archivio.cancella_esame(345615, "444GG"),False)#matricola non presente
    testFalliti += testEqual(archivio.cancella_esame(345655, "564GG"),True)
    testFalliti += testEqual(archivio.cancella_esame(345655, "456FF"),False) #codice non presente

# test su file
    print("==========> Test 12")
    archivio1 = Archivio()
    archivio2 = Archivio()
    testFalliti += testEqual(archivio1.carica("archivio2.txt"),False) #file non deve essere presente, cancellarlo se presente
    testFalliti += testEqual(confronta_archivi(archivio1,archivio2),True)
    testFalliti += testEqual(archivio.salva("archivio.txt"),True)
    testFalliti += testEqual(archivio2.carica("archivio.txt"),True)
    testFalliti += testEqual(confronta_archivi(archivio,archivio2),True)
    testFalliti += testEqual(archivio.carica("archivio2.txt"),False) #file non presente

#stampa finale archivio
    print("==========> Stampa finale archivio")
    print(archivio)
    # abbiamo finito ?
    if testFalliti == 0:
        print("\t****Test completati -- effettuare la consegna come da README")
    else:
        print("Test falliti: ",testFalliti)


# eseguo i test automatici
controllo()

