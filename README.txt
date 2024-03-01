=========================================================================
ISTRUZIONI per il SECONDO ASSEGNAMENTO PYTHON aa 2023/24
========================================================================
L'assegnamento prevede la realizzazione di un insieme di funzioni per la gestione di 
un insieme di studenti universitari come specificato nel file archivio.pdf.

Come procedere:
(1) realizzare (nel file archivio.py) le funzioni richieste
    seguendo le indicazioni dei commenti in corrispondenza di ciascuna funzione
    e testarle opportunamente
(2) eseguire i test nel file main.py fornito dai docenti (senza modificarlo)
    per effettuare questo test sia main.py che testMy.py che archivio.py
    si devono trovare nella stessa cartella
(3) realizzare (nel file gui.py) la GUI come specificato nel file archivio.pdf (oltre a questo README)
    e testarla opportunamente
(4) se tutti i test vengono superati (Pass) e viene stampato il messaggio finale 
    che invita alla consegna, preparare il file archivio.py per
    la consegna inserendo nome cognome e contatti dei componenti del gruppo
    nell'intestazione.
(5) consegnare su Moodle i file archivio.py e gui.py (ed eventuali file aggiuntivi -- vedi istruzioni sotto)
    entro la data di scadenza indicata su Moodle in un unico file zip.

------------------------------------------------
Cosa contiene questa il compito
------------------------------------------------

archivio.pdf		: file contenente la descrizione dell'assegnamento

archivio.py 		: file che contiene la definizione delle funzioni da realizzare

gui.py              : file in cui inserire il codice della GUI, con gli import necessari per usare l'archivio

main.py, testMy.py     : file per i test finali (NON MODIFICARE)

README			: questo file


========================================================================
ALCUNI SUGGERIMENTI per la realizzazione dell'assegnamento
========================================================================

Conviene realizzare le funzioni richiest seguendo le specifiche nei commenti e
analizzando la struttura dei test del file main.py che usano un aversione aggiornata 
della testEqual() usata durante il corso e disponibile in testMy.py.
Durante lo sviluppo e' consigliato non usare immediatamente i test in main.py
per non avere risultati complessi e di difficile interpretazione. Consigliamo invece
di ispiraresi a main.py per creare dei test propri che permettano di
verificare il funzionamento delle funzioni passo passo durante la realizzazione
secondo il principio del debug incrementale spesso citato a lezione.

Quando si è ragionevolmente sicuri della correttezza di quanto realizzato, passare a test finali
in main.py.
Questi ultimi test verificano le funzionalità basilari delle funzioni richieste stampando
il risultato a video. Se tutti i test sono superati lo studente viene invitato
a effettuare la consegna altrimenti si stampa il numero di test falliti.

E' possibile aggiungere test, che vanno realizzati in un file di nome "moreTest.py"
da consegnare insieme a archivio.py.

Se lo si desidera è possibile definire funzioni ausiliarie per la realizzazione delle 
funzioni richieste o aggiungere nuove funzioni, tuttavia
le nuove funzioni devono essere fornite specifiche chiare
del funzionamento (nei commenti) e test di funzionamento adeguati
 (nel file "moreTest.py")

 ========================================================================
 GUI - Interfaccia grafica utente
 ========================================================================

 Deve essere realizzata un'interfaccia grafica usando il modulo tkinter che permetta almeno di
    - visualizzare il contenuto del archivio
    - inserire un nuovo studente nell'archivio
    - modificare i dati di uno studente
    - cancellare uno studente dall'archivio
    - calcolare la media dei voti di uno studente
    - caricare l'archivio da file
    - salvare l'archivio su file
    - uscire dall'applicazione
 L'aspetto dell'interfaccia viene deciso dallo studente.

 NOTE IMPORTANTI: LEGGERE ATTENTAMENTE
---------------------------------------

1) tutti gli elaborati verranno confrontati fra di loro con tool automatici
   per stabilire eventuali situazioni di PLAGIO. Gli elaborato sono
   ragionevolmente simili verranno scartati.

2) Chi in sede di orale risulta palesemente non essere l'autore del software
   consegnato in uno degli assegnamenti dovra' ripetere l'esame con
   un nuovo progetto

3) Tutti i comportamenti scorretti ai punti 1 e 2 verranno segnalati
   ufficialmente al presidente del corso di laurea

----------------------------
 VALUTAZIONE DELL'ASSEGNAMENTO:
----------------------------

Gli studenti che consegnano una versione funzionante e ragionevolmente
corretta dell'assegnamento entro la data di scadenza accumulano un bonus di 2
punti che verra' sommato al voto finale

La modalità di valutazione degli assegnamenti è descritta in archivio.pdf.
