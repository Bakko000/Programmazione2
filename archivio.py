# Corrado Baccheschi
# Matricola 599107

############################################ archivio.py #####################################################################################################################################################################################

##### Questa personalizzata per "alleggerire" --- DRY
### Verifica che il voto sia un intero positivo tra 18 e 33
def checkvoto(num):
     if type(num)!=int or num <= 0 or num >= 33 or num < 18:
        print("Il voto inserito non è corretto. Assicurarsi che", num, " sia un numero compreso tra 18 e 33") 
        return False
     else:
        return True

#### Questa personalizzata per "alleggerire" le funzioni 
def exists_in_tup_list(lista, val, index):
    for tupla in lista:     ### per ogni tupla in lista
        if tupla and tupla[index] == val:  ##controlla che ad un certo indice di tupla corrisponda un certo valore cercato
            print("Il valore " + str(val) + " è già presente all'interno della lista selezionata")
            return True
    return False

# Anche questa personalizzata per evitare di ripetere troppi print
def exists_in(diz, mat):
        if mat in diz.keys():   ### controlla che un elemento esista nelle chiavi del dizionario
           return True
        print("Lo studente con matricola " + str(mat) + " inserita non è presente nell'archivio")
        return False 


class Studente:

    def __init__(self, cognome, nome, matricola):
        if not isinstance(cognome, str) or not cognome.isalpha():  # Controlla che il cognome sia stringa e contenenti caratteri alfanumerici
            raise TypeError('Il cognome deve essere una stringa contenente solo caratteri alfabetici')
        if not isinstance(nome, str) or not nome.isalpha():
            raise TypeError('Il nome deve essere una stringa contenente solo caratteri alfabetici')
        if not isinstance(matricola, int):   ### controlla la matricola che sia un intero
            raise TypeError("La matricola deve essere un intero")
        if matricola<=0:
            raise ValueError("La matricola deve essere un numero positivo")
    
        self.nome = nome
        self.cognome = cognome
        self.matricola = matricola
        self.listaesami = []  ##istanzia la listaesami inizialmente come lista vuota

#- Setters: metodi che modificano il valore di una variabile di istanza, es: set_cognome(cognome) --> modifica il cognome
#   controllare che i valori inseriti siano del tipo e del valore corretto altrimenti sollevare un'eccezione TypeError o ValueError

    def set_cognome(self, new_cognome):
        # Controlla che il cognome sia stringa e contenenti caratteri alfanumerici
        if not isinstance(new_cognome, str) or not new_cognome.isalpha():
            raise TypeError("Il cognome deve essere una stringa contenente solo caratteri alfabetici")
        self.cognome = new_cognome

    def set_nome(self, new_nome):
        # Controlla che il nome sia stringa e contenenti caratteri alfanumerici
        if not isinstance(new_nome, str) or not new_nome.isalpha():
            raise TypeError("Il nome deve essere una stringa contenente solo caratteri alfabetici")
        self.nome = new_nome
    
    def set_matricola(self, new_matricola):
        # Esegue tutti i controlli necessari sulla matricola (intero positivo)
        if type(new_matricola) != int:
            raise TypeError("La nuova matricola deve essere un intero")
        if new_matricola<=0:
            raise ValueError("La nuova matricola deve essere un numero positivo")
        self.matricola = new_matricola

    def set_listaesami(self, new_listaesami):
        if type(new_listaesami) != list:
            raise TypeError("La nuova listaesami deve essere una lista")
        for esame in new_listaesami:  # per ogni esame nella lista esami [(ESAME),..]
            # Se le seguenti condizioni non si realizzano mostra i relativi raise di errore
            if not (type(esame) == tuple and len(esame) == 2 and type(esame[0]) == str and type(esame[1]) == int):
                raise TypeError("Ogni esame deve essere una tupla (codice, voto) con codice di tipo stringa e voto di tipo intero") 
            if not (esame[0] != "" and  checkvoto(esame[1])): 
                raise ValueError("Il codice non deve essere vuoto e il voto deve essere compreso tra 18 e 33")
        self.listaesami = new_listaesami  # tutto va a buon fine, imposta la nuova listaesami
    

# - Getters: metodi che restituiscono il valore di una variabile di istanza, 
# es: get_cognome() --> restituisce il cognome

    def get_cognome(self):
        return self.cognome
    
    def get_nome(self):
        return self.nome
    
    def get_matricola(self):
        return self.matricola
    
    def get_listaesami(self):
        return self.listaesami

    def get_voto(self,codice):
        for esami in self.listaesami: # per ogni esame nella listaesami
            if esami[0] == codice:  # se il codice è stato trovato
                return esami[1] # restituisci il voto 
        return None  # altrimenti non è stato trovato nulla

    def __str__(self):
        # se la listaesami non è vuota, serializzala come stringa altrimenti mostra "no"
        esami_str = self.listaesami if self.listaesami else "no"
        stringa = self.nome + " " + self.cognome + " mat: " + str(self.matricola) + " esami: " + str(esami_str)
        return stringa
    
    def __eq__(self,altroStudente):
        if(self.cognome == altroStudente.get_cognome() and self.nome == altroStudente.get_nome() and self.matricola == altroStudente.get_matricola()):
            return True
        return False
        
    def registra_esame(self,codice,voto):
            if not checkvoto(voto):   # controlla che il voto sia ammissibile
                return False
            if not codice or type(codice) != str: # controlla che il codice sia una stringa non vuota
                return False
            if exists_in_tup_list(self.listaesami, codice.upper(), 0): # chiama la funzione di controllo di esistenza di un valore in una lista di tuple, in questo caso il codice
                     return False
            self.listaesami.append((codice, voto)) # se il codice esiste appende alla lista la nuova tupla
            return True

    def modifica_voto(self,codice,voto):
            if(checkvoto(voto)): # controlla che il voto sia ammissibile
                for i in range(len(self.listaesami)): #scorre la lista esami
                        esame = self.listaesami[i] # ottiene la tupla
                        if esame[0] and esame[0] == codice: # verifica codice
                            self.listaesami[i] = (codice, voto) #aggiorna tupla
                            return True
                return False
            return False

    def cancella_esame(self,codice):
                for i in range(len(self.listaesami)): # scorre 
                        esame = self.listaesami[i]
                        if esame[0] and esame[0] == codice: # verifica
                            del self.listaesami[i] # elimina la tupla (codice, voto) corrispondente
                            return True
                return False
    
    def media(self):
        somma = 0  # Inizializzo la somma a 0 ed anche l'indice i
        i =  0
        f = 0
        if(self.listaesami):
            for tupla in self.listaesami:  # scorro la lista di tuple [(codice, voto)i, (codice, voto)i...i a n]
                somma += tupla[1]  # accumulo una somma sui voti presi
                i += 1
                f = float(somma/i)   # che divido per il numero di esami (i= scorrimenti del for)
            return f
        else:
            return None

##################################

class Archivio:

    def __init__(self):
        self.stud = {}        # inizializzo come dizionario vuoto

    class MatricolaEsistenteError(Exception):
        pass    

    def inserisci(self, studente, note=""):
        try:
            # controllo che sto passando un oggetto di una classe
            if not isinstance(studente, Studente):
                raise TypeError("Lo studente deve essere un'istanza di una classe")
            matricola = studente.get_matricola() # ottengo la matricola
            if exists_in(self.stud, matricola):  # chiamo la funzione di controllo della matricola se esiste 
                raise self.MatricolaEsistenteError("La matricola inserita è già esistente")
            if not isinstance(note, str): # controllo che le note siano stringa
                raise TypeError("Il parametro note deve essere una stringa")
            self.stud[matricola] = (studente, note) # i controlli finiscono bene, aggiungo lo studente all'archivio
            return True
        except (TypeError, ValueError) as e:
            print(f"Errore: {e}")
            return False
        except self.MatricolaEsistenteError as e:
            print(f"Errore: {e}")
            return False

    def elimina(self,matricola):
        if not exists_in(self.stud, matricola): # chiamo la funzione che controlla l'esistenza di una matricola
             return False
        del self.stud[matricola] #se esiste, elimino lo studente
        return True

    def get_note(self,matricola):
        if not exists_in(self.stud, matricola): # chiamo la funzione che controlla l'esistenza di una matricola
            return None
        return self.stud[matricola][1] # se esiste ne torno le note

    def get_studenti(self):
         return list(self.stud.keys()) # torno la lista di chiavi del dizionario (le matricole)

    def modifica_note(self,matricola,nota):
        if not exists_in(self.stud, matricola): # chiamo la funzione che controlla l'esistenza di una matricola
               return False
        if not isinstance(nota, str): # controllo che le nuove note siano stringa
                return False
        self.stud[matricola] = (self.stud[matricola][0], nota) # se i controlli vanno a buon fine, modifico lo studente con le nuove note
        return True

    def __str__ (self):
        result = "" # inizializzo stringa vuota
        for studente in self.stud.values():  # per ogni studente del dizionario
            result += str(studente[0]) + "\n" # accumulo nella stringa tutti gli studenti separati da una nuova riga
            print(result)  # stampo ogni riga
        return result

    def studente(self,matricola):
        if not exists_in(self.stud, matricola): # chiamo la funzione che controlla l'esistenza di una matricola
            return None
        s = self.stud[matricola][0] # se la matricola esiste, torno s che rappresenta un oggetto studente
        return s

    def registra_esame(self,matricola,codice,voto):
            if not exists_in(self.stud, matricola): # chiamo la funzione che controlla l'esistenza di una matricola
                return False           
            if not checkvoto(voto): # controlla con la funzione che il voto sia ammissibile
                return False
            studente = self.studente(matricola) # se i controlli superiori vanno a buon fine, ottengo lo studente con il metodo di classe
            # controllo poi se il codice esiste già in carriera dello studente
            if exists_in_tup_list(studente.get_listaesami(), codice.upper(), 0):
                 return False
            # aggiungo la tupla [(codice, voto)] alla lista esami dello studente
            new_lista_esami = studente.get_listaesami() + [(codice, voto)]
            studente.set_listaesami(new_lista_esami) # infine la controllo e la imposto correttamente
            return True

    def modifica_voto(self,matricola,codice,voto):
            if not exists_in(self.stud, matricola): # chiamo la funzione che controlla l'esistenza di una matricola
                return False
            if not checkvoto(voto): # controlla che il voto sia ammissibile
                return False    
            studente = self.studente(matricola) # se i controlli superiori vanno a buon fine, ottengo lo studente con il metodo di classe
            lista_esami = studente.get_listaesami() # ottengo inoltre la lista esami utilizzando il metodo dell'oggetto studente
            for i in range(len(lista_esami)): # scorro la lista di tutti gli esami
                esame = lista_esami[i] # ottengo tupla (codice, voto)
                if esame[0] == codice: # controllo che il codice esista
                    lista_esami[i] = (codice, voto)  # se esiste, sostituisco alla tupla una nuova tupla con stesso codice ma diverso voto
                    studente.set_listaesami(lista_esami) # controllo e imposto correttamente la nuova lista esami
                    return True
            print(f"Il codice {codice} non è presente nella lista esami dello studente")
            return False

    def cancella_esame(self,matricola,codice):
            if not exists_in(self.stud, matricola): # chiamo la funzione che controlla l'esistenza di una matricola
                return False
            studente = self.studente(matricola) # ottengo i dati dello studente
            lista_esami = studente.get_listaesami() # ottengo la sua lista esami
            for i in range(len(lista_esami)): #scorro la lista di tuple
                esame = lista_esami[i]  # (codice,voto)
                if esame[0] == codice: # se il codice esiste
                    del lista_esami[i] # cancello la tupla (codice, voto)
                    return True
            else:
                print(f"Il codice {codice} non è presente nella lista esami dello studente")
                return False

    def media(self, matricola):
            if not exists_in(self.stud, matricola): # chiamo la funzione che controlla l'esistenza di una matricola
                return None
            studente = self.studente(matricola)
            somma = 0  # Inizializzo la somma a 0 ed anche l'indice i
            i =  0
            f = 0
            for tupla in studente.get_listaesami():  # scorro la lista di tuple [(codice, voto)i, (codice, voto)i...i a n]
                somma += tupla[1]  # accumulo una somma sui voti presi
                i += 1
                f = float(somma/i)   # che divido per il numero di esami (i= scorrimenti del for)
            return f

    def lista_studenti_promossi(self,codice,soglia=18):
        lista = [] # lista inizialmente vuota
        for matricola in self.get_studenti(): # scorro ogni matricola nella lista di matricole restituita dal metodo di classe
            studente = self.studente(matricola)  # ottengo lo studente
            if studente: # se non è vuoto
                esami = studente.get_listaesami() # ottengo i suoi esami
                for esame in esami: # per ogni tupla (codice, voto) in carriera
                    if codice and esame[0] == codice and esame[1] >= soglia: # se il primo elemento della tupla (codice) è trovato ed il secondo elemento (voto) è maggiore della soglia
                        lista.append((studente.get_nome(), studente.get_cognome(), studente.get_matricola())) # appendo nome, cognome e matricola dello studente alla lista 
        return lista

    def conta_studenti_promossi(self, codice, soglia=18):
            return len(self.lista_studenti_promossi(codice, soglia)) # ritorno semplicmenete la lunghezza (len) della lista sopra

    def lista_studenti_media(self, soglia=18):
        lista = []
        for matricola in self.get_studenti(): # scorro ogni matricola nella lista di matricole restituita dal metodo di classe
            avg = self.media(matricola) # faccio una media degli esami di ogni matricola con il metodo di classe
            if avg is not None and avg >= soglia: # se la media non è 0 ed è superiore alla soglia
                studente = self.studente(matricola) # ottengo i dati dello studente
                lista.append((studente.get_nome(), studente.get_cognome(), studente.get_matricola(), avg))
        return lista

    def salva(self,nomefile):
        data = self.get_studenti() # Ottengo archivio attuale
        if not data: # Se è vuoto, non permetto il salvataggio
           print("Errore il file salvato non può essere vuoto")
           return False
        else: # Altrimenti procedo a salvare
            # Assicura che il file finisca con txt
            if not nomefile.endswith(".txt"):
                nomefile += ".txt"
            try: # provo e gestisco eccezioni
                with open(nomefile, 'w') as file: #apro in scrittura il file
                    for matricola in self.get_studenti(): # per ogni matricola
                        studente = self.studente(matricola) # ottengo lo studente relativo 
                        file.write(f"Matricola: {studente.get_matricola()}\n") # scrivo su file tutti i dati usando i metodi della classe studente
                        file.write(f"Nome: {studente.get_nome()}\n")
                        file.write(f"Cognome: {studente.get_cognome()}\n")
                        file.write(f"Esami: {studente.get_listaesami()}\n")
                        file.write(f"Note: {self.get_note(studente.get_matricola())}\n")
                        file.write("\n") 
                return True
            except IOError as e:   # eccezione di tipo IO su file
                print(f"Errore durante il salvataggio: {e}")
                return False

    def carica(self, nomefile):
        # Assicura che il file finisca con txt
        if not nomefile.endswith(".txt"):
            nomefile += ".txt"
        try:
            with open(nomefile, 'r') as file:
                data = False # assumo inizialmente che non ci siano dati nel file
                for line in file: #  Itera su ogni linea del file
                    if line.startswith("Matricola:"): # verifica se la riga inizia con "Matricola". 
                        matricola = int(line.split(":")[1].strip()) # Se sì, estrae il valore della matricola dalla riga,  rimuove eventuali spazi vuoti e lo converte in un intero 
                    elif line.startswith("Nome:"): # verifica se inizia con Nome:
                        nome = line.split(":")[1].strip() # Se sì, estrae il valore dalla riga e rimuove spazi vuoti 
                    elif line.startswith("Cognome:"): # verifica se inizia con cognome..
                        cognome = line.split(":")[1].strip() # assegna, splitta e rimuove spazi
                    elif line.startswith("Esami:"): # come i precedenti
                        esami = eval(line.split(":")[1].strip()) # ^
                    elif line.startswith("Note:"): # ^
                        note = line.split(":")[1].strip() # ^
                    elif line == "\n": # se viene rilevata una riga vuota ("\n"), tutte le informazioni relative a uno studente sono state lette, creiamo perciò lo studente
                        studente = Studente(cognome, nome, matricola) # istanzio oggetto della classe 
                        studente.set_listaesami(esami) # imposto la lista esami
                        inserisci = self.inserisci(studente, note) # e verifico che l'inserimento vada a buon fine
                        if not inserisci: # Se ci sono duplicati di matricole 
                             return False # interrompi
                        data = True # altrimenti se sono stati letti dati dal ciclo, data è True e proseguo
                if not data: # se data non è True, il file è vuoto
                    print("Errore: il file caricato non può essere vuoto")
                    return False
            return True
        except FileNotFoundError:   # Il file non è stato trovato
             print("File non trovato.")
             return False
        except IOError as e:
            print(f"Errore durante il caricamento dell'archivio: {e}")
            return False
        
##################################################### END ##############################################################################################################################################################################################
