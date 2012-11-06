5.2 Bisezione, sqrt

* Scrivere una nuova funzione sqrt
  * Parametro x e risultato di tipo float
  * Restituire risultato con errore minore di 0.0001
* In un ciclo, trovare approssimazioni successive:
  * Due variabili low, high: inizio e fine intervallo di stima (intervallo iniziale: da 0 ad x, oppure da 0 ad 1, se x<1)
  * Si pone la stima y a metà intervallo
  * Se y*y - x > 0, nel seguito si considera solo la prima metà dell'intervallo (da low ad y)
  * Altrimenti solo la seconda metà (da y ad high)
  * Ad ogni iterazione si dimezza l'intervallo residuo
