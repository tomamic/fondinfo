4.7 Zig zag

* Scrivere una funzione per riempire di numeri crescenti una matrice
* Seguire il percorso a zig-zag suggerito (figura nellla slide)
  * Partire dall'angolo in basso a sinistra, la direzione iniziale è in diagonale, verso basso-destra
  * Spostarsi nella cella libera a destra e avanzare in diagonale, verso alto-sinistra
  * In generale, quando si arriva al bordo, spostarsi nella cella libera più vicina e invertire la direzione
* Dimensioni indicate dall'utente a runtime

_Tenere traccia della direzione attuale (∆y, ∆x)_

_Avanzare fino al bordo, poi invertire la direzione_
