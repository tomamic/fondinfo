# Progetto 2. Pong

* Realizzare un gioco con diversi personaggi
* Classe per partita; classe base astratta (e sottoclassi) per personaggi
* Polimorfismo nei vari personaggi, per:
  * Il movimento
  * L'interazione reciproca

## Base

* Campo rettangolare
* Pallina: si muove a 45°, rimbalza su bordi lunghi e barrette
* Barrette: si muovono solo verticalmente
* Punti: segnati quando la pallina esce dal campo

_È fornito un semplice framework di esempio_

## Doppio

* Sottoclasse di barretta: movimento automatico
* Partita di “doppio”
  * 2 squadre, 2 barrette per ogni squadra
  * Barrette distanziate (una più avanti e una più dietro)
  * Movimento sempre e solo in verticale
* A piacimento: ulteriori palline, ostacoli, bonus...

## Opzionale

* Garantire ai personaggi un movimento libero, pixel a pixel (posizione x, y non fissata su una griglia rigida)
* Angolo di rimbalzo della palla sulla barretta dipendente da distanza dal centro della barretta
* Usare un oggetto QPainter nel metodo paintEvent, oppure...
* Una QGraphicsScene (con gli associati QGraphicsItem e QGraphicsView)
