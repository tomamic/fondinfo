4.5 Lancio dadi

* Come es. 2.4, ma ad ogni giocata l'attaccante (A) lancia 3 dadi, il difensore (D) 2 dadi
* Una funzione (due vector come parametri) confronta a coppie i dadi:
  * il dado migliore di A con quello migliore di D,
  * poi il dado medio di A con quello peggiore di D
* I dadi di ciascun giocatore vanno ordinati:
  * sort(v.begin(), v.end())
* Stimare la probabilità dei diversi risultati
  * 0, 1 o 2 punti dell'attaccante
* Ripetere l'esperimento con diversi numeri di dadi
