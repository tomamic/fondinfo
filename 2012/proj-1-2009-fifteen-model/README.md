# Progetto 1. Gioco del quindici

* Classe per incapsulare dati e regole di un gioco
  * Campi privati + metodi pubblici (e _privati_)
* Ciclo principale e interazione con l'utente al di fuori della classe
  * I/O, inizialmente tramite console

## Base

* Tabella rettangolare: size = rows x columns
* Nella tabella ci sono size - 1 tessere, numerate progressivamente
* Inizio della partita
  * Le tessere sono prima disposte tutte in ordine, poi mescolate
* Il mescolamento richiede di spostare ripetutamente una delle tessere...
  * ... tra quelle adiacenti alla cella vuota
  * La scelta della tessera da spostare è ogni volta casuale
* L'utente sceglie ad ogni turno quale tessera spostare...
  * ... tra quelle adiacenti alla cella vuota
* La partita termina quando le tessere sono tutte in ordine, con la cella vuota in fondo

## Gui

* Aggiungere una interfaccia grafica al progetto
  * Creare una sottoclasse di QWidget
  * Rendere l'interfaccia adattabile a dimensioni diverse del campo di gioco
* Riuso - Definire la classe di modello per le partite in modo generico
  * Usabile sia da interfaccia grafica che da console

## Emissione segnale

* Dopo una mossa corretta, il modello emette un segnale
* In questo modo l'interfaccia può aggiornale sole le caselle cambiate
