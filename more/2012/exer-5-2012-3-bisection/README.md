5.3 Bisezione, ricorsione

* Trovare lo zero di una funzione
  * f(x) = x3 – x – 1, per 1 ≤ x ≤ 2
  * Trovare x t.c. |f(x)| < 0.001
* Definire una funzione ricorsiva findZero
  * Parametri necessari: inizio intervallo di ricerca, fine intervallo di ricerca
* Bisezione: invocare ad ogni livello la funzione su un intervallo dimezzato

5.2 Bisezione, iterazione

* Trovare lo zero di una funzione
  * f(x) = x3 – x – 1, per 1 ≤ x ≤ 2
  * Trovare x t.c. |f(x)| < 0.001
* Dimezzare ripetutamente l'intervallo considerato:
  * Variabili per inizio e fine intervallo di ricerca - All'inizio: min = 1; max = 2;
  * Si pone la stima x a metà intervallo e si calcola f(x)
  * Se l'errore è accettabile, x è il risultato
  * Altrimenti se f cambia segno tra min ed x, si ripete il ciclo considerando solo la prima metà dell'intervallo
  * Altrimenti solo la seconda metà (da x ad max)
