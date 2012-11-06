4.4 Vettore di punti

* Gestire un vettore di puntatori a punti
  * vector<Point*> points;
* Ripetutamente chiedere all'utente di scegliere tra:
  * Aggiunta di un nuovo punto: Point* pt = new Point(x, y); // ...
  * Eliminazione di un punto esistente (deallocazione memoria + rimozione puntatore): delete points[i]; // ...
  * Calcolo della distanza tra due punti scelti dall'utente
* Al termine di ogni operazione dell'utente, visualizzare la posizione attuale di tutti i punti
