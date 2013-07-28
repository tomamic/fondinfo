# Progetto 1. Prato fiorito

* Classe per incapsulare dati e regole di un gioco
  * Campi privati + metodi pubblici (e _privati_)
* Ciclo principale e interazione con l'utente al di fuori della classe
  * I/O, inizialmente tramite console

## Base

* N fiori nascosti a caso in una tabella rettangolare
* L'utente sceglie una casella da scoprire, ad ogni turno
  * Se c'è fiore, partita persa
  * Altrimenti, conteggio fiori nelle caselle adiacenti
* Se restano solo caselle con fiori, partita vinta

## Ricorsione

* Prato di varie dimensioni
* Quando viene scoperto uno “0”, si scoprono anche le celle adiacenti (ricorsione)
* L'utente può marcare una cella con una bandiera; se ci sono N bandiere:
  * Partita vinta (tutte su fiori)
  * Altrimenti persa
* Si può salvare una partita su file e poi ricaricarla

## Gui

* Aggiungere una interfaccia grafica al progetto
  * Creare una sottoclasse di QWidget
  * Rendere l'interfaccia adattabile a dimensioni diverse del campo di gioco
* Riuso - Definire la classe di modello per le partite in modo generico
  * Usabile sia da interfaccia grafica che da console

_Sono fornite due classi per gestire anche i click con il tasto destro del mouse_

