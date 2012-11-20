5.1 Battaglia in classe

* Classe per incapsulare le funzionalità dell'es. 4.3
* Il costruttore riceve rows, cols e alloca la matrice
  * Es. campo privato: vector<char> matrix;
  * Nel costruttore: matrix.assign(rows*cols, '.')
* Metodo per l'inserimento casuale di una nave di dimensione size (size parametro del metodo)
* Metodo per la stampa dello stato su generico stream
  * Parametro ostream & out, passato per riferimento
* In main: creare un oggetto, inserire diverse navi a scelta dell'utente, infine scrivere la matrice su file

4.3 Battaglia navale

* Allocare una matrice rows×cols (dimensioni scelte dall'utente), ex.:
  * vector< vector<char> > matrix(rows, vector<char>(cols, '-'));
  * vector<char> matrix(rows*cols, '-');
* Ripetutamente...
  * Chiedere all'utente un numero size
  * Riempire con '+' un numero size di celle adiacenti (direzione e posizione di partenza casuali)
  * Accettabili inserimenti sovrapposti o parziali, fino a bordo
  * Mostrare la matrice risultante
* Al termine salvare la matrice in un file di testo
