from archivio import * 
import tkinter as tk
import sys
from tkinter import messagebox

# L'applicazione è un piccolo gestionale per studenti che permette diverse azioni, la maggior parte legate al numero di matricola.
# Per ottenere tutti i dati di uno studente e controllare la correttezza della matricola, il metodo retrieve_data gestisce tutte le eccezioni e gli errori oppure restituisce l'oggetto studente. Esso viene richiamato dagli altri metodi.
# Dalla home con un piccolo input entry "Inserire Matricola" è possibile aprire diverse finestre:
# - Eliminare uno studente, controllando la volontà certa dell'utente di eseguire una tale operazione "critica", attraverso un messaggio di conferma;
# - Modificare uno studente, controllando la correttezza dei nuovi parametri e valori inseriti;
# - Registrare un esame allo studente, con i controlli sulla validità del voto e sulla non esistenza del nuovo codice in carriera;
# - Modificare un voto per un esame allo studente, con i controlli sul voto e sull'esistenza del codice dell'esame cercato;
# - Calcolare la media dello studente, arrotondata di 2, mostrata come valore o come 0 se nessun esame è stato ancora sostenuto;
# E' inoltre possibile SENZA un numero di matricola preinserito:
# - Inserire uno studente, tramite un'interfaccia grafica, con i controlli sulla correttezza e validità dei campi da compilare come nome, cognome, matricola e note;
# - Uscire dall'applicazione, confermata attraverso un messaggio di conferma, prima di proseguire con l'interruzione del programma.
# Sono inoltre possibili operazioni I/O su file, in questo caso per l'Archivio:
# - La classe master per operazioni I/O è ArchivioIOOper, con le sue sottoclassi per le diverse operazioni possibili:
#     - sottoclasse LoadArchivio - che si occupa di caricare un nuovo archivio nell'app da file nel sistema
#     - sottoclasse SalvaArchivio - che salva in un file del sistema l'archivio corrente

 
############################### Classe principale per Home della GUI ###############################
class HomeGUI:
    def __init__(self, root):
        self.root = root
        self.my_archivio = Archivio() # Istanzio l'oggetto Archivio
        self.root.title("Gestionale per carriera studenti")
        # Configura un background color
        self.root.configure(bg="#F5F5DC")
        # Configura grandezza finestra
        self.root.geometry("600x450") 
    
        # Crea frames per ogni colonna
        frame1 = tk.Frame(self.root, bg="#F5F5DC")
        frame1.pack(side="left", fill="both", expand=True)

        frame2 = tk.Frame(self.root, bg="#F5F5DC")
        frame2.pack(side="right", fill="both", expand=True)

        # Bottoni nella prima colonna
        self.insert_student_button = tk.Button(frame1, text="Inserisci Studente", command=self.insert_student, fg="white", bg="#996633", width=15, height=2)
        self.insert_student_button.pack(side="top", anchor="n", pady=15)

        self.del_button = tk.Button(frame1, text="Elimina Studente", command=self.elimina, fg="white", bg="#996633", width=15, height=2)
        self.del_button.pack(side="top", anchor="n", pady=15)

        self.regex_button = tk.Button(frame1, text="Registra esame", command=self.regex_apri, fg="white", bg="#996633", width=15, height=2)
        self.regex_button.pack(side="top", anchor="n", pady=15)

        self.load_button = tk.Button(frame1, text="Carica archivio", command=self.load_apri, fg="white", bg="#996633", width=15, height=2)
        self.load_button.pack(side="top", anchor="n", pady=15)

        self.load_button = tk.Button(frame1, text="Salva archivio", command=self.save_apri, fg="white", bg="#996633", width=15, height=2)
        self.load_button.pack(side="top", anchor="n", pady=15)

        # Bottoni nella seconda colonna
        self.edit_button = tk.Button(frame2, text="Modifica Studente", command=self.apri_modifica_stud, fg="white", bg="#996633", width=15, height=2)
        self.edit_button.pack(side="top", anchor="n", pady=15)

        self.edit_button = tk.Button(frame2, text="Media voti studente", command=self.calc_media, fg="white", bg="#996633", width=15, height=2)
        self.edit_button.pack(side="top", anchor="n", pady=15)

        self.edit_button = tk.Button(frame2, text="Modifica Voto", command=self.modvoto_apri, fg="white", bg="#996633", width=15, height=2)
        self.edit_button.pack(side="top", anchor="n", pady=15)

        self.edit_button = tk.Button(frame2, text="Visualizza Archivio", command=self.view_archv, fg="white", bg="#996633", width=15, height=2)
        self.edit_button.pack(side="top", anchor="n", pady=15)

        self.exit_button = tk.Button(frame2, text="Esci", command=self.exit, fg="white", bg="red", width=15, height=2)
        self.exit_button.pack(side="top", anchor="n", pady=15)
        
        # Label per l'entry della matricola
        self.del_label = tk.Label(frame1, text="Inserire Matricola", bg="#F5F5DC")
        self.del_label.pack(side="top", anchor="n", pady=5)
        
        # Entry della matricola
        self.entry = tk.Entry(frame1, width=30)
        self.entry.pack(side=tk.RIGHT, anchor="n", pady=5)

####### Metodi per le finestre in relazione alle azioni possibili###########
        
### Uscita e chiusura di tutte le finestre e dall'applicazione
    def exit(self):
        # Apre una finestra di conferma prima di uscire
        confirm = messagebox.askyesno("Exit", "Sei sicuro di uscire?")
        if confirm:
            sys.exit() # interrompe l'esecuzione ed esce

#### Metodo generico di ottenimento e test dei dati studente se disponibili, richiamato dagli altri metodi
    def retrieve_data(self):
        try:
            matricola = self.entry.get() # ottiene la matricola dall'entry della home
            matricola = int(matricola) # converte in un intero perchè restituita sempre come stringa
            studente = self.my_archivio.studente(matricola) # cerca di ottenere lo studente
            if studente is not None:
                return studente   # se esiste restituisco l'oggetto con i suoi dati
            else:
                messagebox.showerror("Errore", f"Nessuno studente trovato con la matricola {matricola}")
        except (TypeError) as e:
            messagebox.showerror("Errore", str(e))
        except (ValueError) as e:
            messagebox.showerror("Errore", str("Assicurarsi che la matricola sia un numero positivo."))
        return False
    
#### Apre finestra visualizza archivio
    def view_archv(self):
        window = tk.Tk()     # apre una nuova finestra e setta grafica generale
        window.configure(bg="#F5F5DC")
        window.geometry("600x600")
        window.title("Archivio")
        # Ottiene i dati dal metodo str dell'Archivio serializzandolo
        formatted_data = str(self.my_archivio)
        if(formatted_data):  # se non è vuoto
            label = tk.Label(window, text=formatted_data, justify='left')  # mostro i dati
        else:
            label = tk.Label(window, text="Archivio vuoto.", justify='left') # altrimenti mostro la scritta "Archivio vuoto"
        label.pack(padx=10, pady=10)

### Gestisce eliminazione studente
    def elimina(self):
            studente = self.retrieve_data() # chiama la funzione retrieve data per controllare esistenza studente con data matricola
            if(studente):   # se lo studente esiste mostra un messaggio prima di proseguire con un'operazione "critica" di eliminazione
                risposta = messagebox.askyesno("Conferma", "Vuoi davvero eliminare lo studente " + studente.get_nome() + " " + studente.get_cognome() + " ?")
                if(risposta):   # se la risposta è positiva ottengo la matricola e chiamo il metodo della classe per eliminarla 
                    success = self.my_archivio.elimina(studente.get_matricola()) # elimino
                    if success:
                        messagebox.showinfo("Success", "Studente eliminato con successo.") # fine, restituisco messaggio di avvenuta eliminazione
                    else:
                        messagebox.showerror("Errore", "Errore nella cancellazione dello studente.")

### Apre la finestra di calcolo della media 
    def calc_media(self):
            student_data = self.retrieve_data() # chiama la funzione retrieve data per controllare esistenza studente con data matricola
            if (student_data):
                media_result = self.my_archivio.media(student_data.get_matricola()) # chiamo il metodo media con cui calcolo la media dello studente
                media = round(media_result, 2) # arrotondo la media
                media_window = tk.Toplevel(self.root)
                media_window.title("Media Studente")
                media_label = tk.Label(media_window, text=f"Media dello studente: {media}", fg="white", bg="#996633")  # mostro la media
                media_label.pack()
                media_window.mainloop()

    ### Apre l'interfaccia di registrazione del voto
    def regex_apri(self):
            student_data = self.retrieve_data() # chiama la funzione retrieve data per controllare esistenza studente con data matricola
            if (student_data):
                # Crea una nuova finestra
                exam_window = tk.Tk()
                exam_window.configure(bg="#F5F5DC")
                exam_window.title("Registra un nuovo esame")
                # Label per codice e voto              
                codice_label = tk.Label(exam_window, text="Codice Esame:")
                voto_label = tk.Label(exam_window, text="Voto:")
                    # Entry widgets
                codice_entry = tk.Entry(exam_window)
                voto_entry = tk.Entry(exam_window)
                    # Bottone per registrare un nuovo esame, attiva il metodo di registrazione
                register_button = tk.Button(exam_window, text="Registra", fg="white", bg="#996633", command=lambda: self.register_exam(student_data, codice_entry.get(), voto_entry.get(), exam_window))
                    # Pack
                codice_label.pack()
                codice_entry.pack()
                voto_label.pack()
                voto_entry.pack()
                register_button.pack()
                exam_window.mainloop()
            
    ################ Gestisce registrazione esame
    def register_exam(self, studente, codice, voto, window):
        try:
            self.voto=int(voto) # prova a convertire l'entry del voto restituito in stringa, in int 
            success = studente.registra_esame(codice.upper(), self.voto) # e prova a registrare l'esame
            if success:
                messagebox.showinfo("Success", "Voto aggiunto con successo.")
            else:
               messagebox.showerror("Errore", "Il codice esiste già o i parametri non sono corretti.")
        except(TypeError) as e:      # altrimenti il voto non è convertibile in intero
            messagebox.showerror("Errore", str("Assicurarsi che voto e numero siano del tipo corretto."))
        except(ValueError) as e:  # o il voto era vuoto o inferiore a 18 o maggiore di 32
            messagebox.showerror("Errore", str("Assicurarsi che i valori siano corretti e non vuoti."))

        window.destroy()  # alla fine esco dalla finestra


 ### Apre l'interfaccia di modifica di voto
    def modvoto_apri(self):
            student_data = self.retrieve_data() # chiama la funzione retrieve data per controllare esistenza studente con data matricola
            if (student_data):
                # Crea una nuova finestra
                window = tk.Tk()
                window.configure(bg="#F5F5DC")
                window.title("Modifica voto per lo studente")
                # Label per codice e voto              
                codice_label = tk.Label(window, text="Codice Esame:")
                voto_label = tk.Label(window, text="Voto:")
                    # Entry widgets
                codice_entry = tk.Entry(window)
                voto_entry = tk.Entry(window)
                    # Bottone per modificare un voto esame, attiva il metodo di modifica ottenendo i valori degli entry input e passandoli al metodo finale
                register_button = tk.Button(window, text="Invia", fg="white", bg="#996633", command=lambda: self.edit_mark(student_data, codice_entry.get(), voto_entry.get(), window))
                    # Pack
                codice_label.pack()
                codice_entry.pack()
                voto_label.pack()
                voto_entry.pack()
                register_button.pack()
                window.mainloop()

### Gestisce modifica voto
    def edit_mark(self, studente, codice, voto, window):
        try:
            self.voto=int(voto) # prova a convertire l'entry del voto restituito in stringa, in int 
            success = self.my_archivio.modifica_voto(studente.get_matricola(), codice.upper(), self.voto) # e prova a modificare il voto per l'esame
            if success:
                messagebox.showinfo("Success", "Voto modificato con successo.")
            else:
               messagebox.showerror("Errore", "Il codice non esiste o i parametri non sono corretti.")
        except(TypeError) as e:      # altrimenti il voto non è convertibile in intero
                messagebox.showerror("Errore", str("Assicurarsi che voto e numero siano del tipo corretto."))
        except(ValueError) as e:  # o il codice o il voto erano vuoto o inferiore a 18 o maggiore di 32
                messagebox.showerror("Errore", str("Assicurarsi che i valori siano corretti e non vuoti."))

        window.destroy()  # alla fine esco dalla finestra

### Apre l'interfaccia di modifica studente
    def apri_modifica_stud(self):
        student_data = self.retrieve_data() # chiama la funzione retrieve data per controllare esistenza studente con data matricola
        if (student_data):
                studente = student_data
                ## Nuova finestra
                editwin = tk.Tk()
                editwin.title("Dettagli e modifica")

            # Labels e entry modificabili 
                editwin.cognome_label = tk.Label(editwin, text="Cognome:")
                editwin.cognome_entry = tk.Entry(editwin, width=30)
                editwin.cognome_entry.insert(0, studente.get_cognome())

                editwin.nome_label = tk.Label(editwin, text="Nome:")
                editwin.nome_entry = tk.Entry(editwin, width=30)
                editwin.nome_entry.insert(0, studente.get_nome())

                editwin.matricola_label = tk.Label(editwin, text="Matricola:")
                editwin.matricola_entry = tk.Entry(editwin, width=30)
                editwin.matricola_entry.insert(0, studente.get_matricola())
                # Assumo che la matricola non rientri nei dati da modificare
                editwin.matricola_entry.configure(state='readonly')

                editwin.note_label = tk.Label(editwin, text="Note:")
                editwin.note_entry = tk.Entry(editwin, width=30)
                # Le note non appartengono alla classe studente, chiamo perciò il metodo get_note di Archivio per ottenerle tramite la matricola
                editwin.note_entry.insert(0, self.my_archivio.get_note(studente.get_matricola()))

                # Grafica generale in grid
                editwin.cognome_label.grid(row=0, column=0, sticky="w")
                editwin.cognome_entry.grid(row=0, column=1, sticky="w")
                editwin.nome_label.grid(row=1, column=0, sticky="w")
                editwin.nome_entry.grid(row=1, column=1, sticky="w")
                editwin.matricola_label.grid(row=2, column=0, sticky="w")
                editwin.matricola_entry.grid(row=2, column=1, sticky="w")
                
                # Formatto adeguatamente la lista degli esami
                esami_text = self.format_esami(studente.get_listaesami())
                editwin.esami_label = tk.Label(editwin, text=f"Esami: {esami_text}")
                editwin.esami_label.grid(row=3, column=0, sticky="w")
                editwin.note_label.grid(row=4, column=0, sticky="w")
                editwin.note_entry.grid(row=4, column=1, sticky="w")
                # Bottone per salvare 
                editwin.save_button = tk.Button(editwin, text="Salva Modifiche", command=lambda:self.salva(editwin, studente), fg="white", bg="#996633")
                editwin.save_button.grid(row=5, column=0, columnspan=2, pady=10, sticky="w")
                editwin.mainloop()

    # Funzione di formattazione degli esami
    def format_esami(self, lista_esami):
        formatted_esami = [] # inizializzo lista vuota
        for codice, voto in lista_esami: # per ogni elemento della tupla
            formatted_esami.append(f"{codice.upper()}: {voto}") # appendo "codice: voto"
        return ", ".join(formatted_esami) # separo con una virgola codice: voto, codice: voto
    
    # Gestione del salvataggio delle modifiche
    def salva(self, editwin, studente):
        new_note = editwin.note_entry.get() # Ottengo l'entry della note
        if new_note.isnumeric():  # ... e controllo se è numerica (non si puo usare str in quanto restituita sempre come stringa in automatico)
                messagebox.showerror("Errore", "La nota non può essere un valore numerico.")
        else:  # se la nota non è numerica posso andare avanti
            try:
                 # Ottengo gli entry input e imposto i nuovi dati con i metodi dello studente (set cognome, set nome)
                new_cognome = editwin.cognome_entry.get()
                new_nome = editwin.nome_entry.get()
                studente.set_cognome(new_cognome)
                studente.set_nome(new_nome)
                # Chiamo il metodo modifica note di archivio dando la matricola per modificare le note
                success = self.my_archivio.modifica_note(studente.get_matricola(), new_note)
                if success: # se tutto va a buon fine restituisco messaggio di avvenuta modifica
                    messagebox.showinfo("Success", "Studente modificato con successo.")
                else:
                    messagebox.showerror("Errore", "Errore: le note devono essere di tipo stringa.")

            except (TypeError, ValueError) as e:
                messagebox.showerror("Errore", str(e))
        editwin.destroy()  # alla fine esco dalla finestra

### Apre l'interfaccia di inserimento studente
    def insert_student(self):
        # Crea una nuova finestra
        insert = tk.Tk()
        insert.title("Inserimento di uno studente")
        insert.configure(bg="#F5F5DC")
        insert.geometry("300x200")

        # Label e entry
        insert.cognome_label = tk.Label(insert, text="Cognome:")
        insert.cognome_entry = tk.Entry(insert)
        insert.nome_label = tk.Label(insert, text="Nome:")
        insert.nome_entry = tk.Entry(insert)
        insert.matricola_label = tk.Label(insert, text="Matricola:")
        insert.matricola_entry = tk.Entry(insert)
        insert.note_label = tk.Label(insert, text="Note:")
        insert.note_entry = tk.Entry(insert)
        # Bottone per il metodo di inserimento 
        insert.insert_button = tk.Button(insert, text="Inserisci", fg="white", bg="#996633", command=lambda:self.insert(insert))

        # Pack e mainloop 
        insert.cognome_label.pack()
        insert.cognome_entry.pack()
        insert.nome_label.pack()
        insert.nome_entry.pack()
        insert.matricola_label.pack()
        insert.matricola_entry.pack()
        insert.note_label.pack()
        insert.note_entry.pack()
        insert.insert_button.pack()
        insert.mainloop()

########## Gestisce metodo di inserimento dello studente
    def insert(self, insert):
        note = insert.note_entry.get() # Ottengo dall'oggetto finestra l'entry della note
        if note.isnumeric():   # Check se note numerico
                messagebox.showerror("Errore", "La nota non può essere un valore numerico.")
        else:  # se non è numerico
            try:
                # Ottengo gli altri entry
                cognome = insert.cognome_entry.get()
                nome = insert.nome_entry.get()
                matricola = insert.matricola_entry.get()
                matricola = int(matricola)
                # Istanzio il nuovo studente
                studente = Studente(cognome, nome, matricola)
                # Chiamo il metodo inserisci per inserirlo assieme alle sue note
                success = self.my_archivio.inserisci(studente, note)
                if success:
                    messagebox.showinfo("Success", "Studente inserito con successo.")
                else:
                    messagebox.showerror("Errore", "Errore nell'inserimento dello studente, controllare i dati inseriti.")

            except self.my_archivio.MatricolaEsistenteError as e:
                messagebox.showerror("Errore", "La matricola inserità è già esistente.")
            except (TypeError) as e:
                messagebox.showerror("Errore", str(e))
            except (ValueError):
                messagebox.showerror("Errore", str("Controllare che i valori inseriti siano corretti."))
            
        insert.destroy() # infine esco

### Apre l'interfaccia di caricamento dell'archivio
    def load_apri(self):
        # Apre una sottoclasse di un master per operazioni su file dell'Archivio
        load_arc = LoadArchivio(self.my_archivio)
        load_arc.run() # avvia la classe

### Apre l'interfaccia di salvataggio dell'archivio
    def save_apri(self):
        # Apre una sottoclasse di un master per operazioni su file dell'Archivio
        load_arc = SalvaArchivio(self.my_archivio)
        load_arc.run() # avvia la classe

################ Classe base per operazioni I/O su file dell'archivio  #####################
######## il tipo di operazione è deciso dal parametro "operation"
####### operation può assumere "salva" o "carica", ma è estendibile
class ArchivioIOOper(HomeGUI):
    def __init__(self, operation):
        ##### Definisce l'interfaccia grafica della finestra per operazioni su file
        self.root = tk.Tk()
        self.root.title(operation)
        self.root.configure(bg="#F5F5DC")
        self.root.geometry("300x300")
        # Label e entry
        self.file_label = tk.Label(self.root, text="Nome del file:")
        self.file_entry = tk.Entry(self.root)
        # Operation = Salva | Carica
        self.button_text = f"{operation} Archivio"
        self.operation_button = tk.Button(self.root, text=self.button_text, fg="white", bg="#996633", command=self.archivio_op)
        self.file_label.pack()
        self.file_entry.pack()
        self.operation_button.pack()

####### Il metodo si occupa di definire una generica operazione su file
    def archivio_op(self):
        # Ottiene il file name
        file_name = self.file_entry.get()
        if file_name:
            success = self.execute(file_name) # Esegue un'operazione su file
            if success:
                messagebox.showinfo("Success", "Operazione conclusa con successo.")
            else:
                messagebox.showerror("Errore", "Si è verificato un errore, controllare che il file non sia vuoto e non contenga duplicati.")
        self.root.destroy()

    def run(self):
        self.root.mainloop()

######## Sottoclasse per salvare archivio
class SalvaArchivio(ArchivioIOOper):
    def __init__(self, my_archivio):
        super().__init__("Salva") # Operation = Salva, button = "Salva"
        self.my_archivio = my_archivio

    def execute(self, file_name):
        return self.my_archivio.salva(file_name) # Con il metodo della classe Archivio salva il file
###### E per caricare archivio
class LoadArchivio(ArchivioIOOper):
    def __init__(self, my_archivio):
        super().__init__("Carica") # Operation = Carica, button = "Carica"
        self.my_archivio = my_archivio

    def execute(self, file_name):
        return self.my_archivio.carica(file_name) # Con il metodo della classe Archivio carica il file

# Avvia l'app
w = tk.Tk()
HomeGUI(w)
w.mainloop()
