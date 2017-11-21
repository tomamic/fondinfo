// Per ognuno dei seguenti pezzi di programma, determinate se c'e` un errore nel codice. 

//--------------- Il codice seguente dovrebbe definire la classe Time:
class Time
{
public:
  Time( int = 0, int = 0, int = 0);
  void setTime( int, int, int );
  void printUniversal();
  void printStandard();

private:
  int hour;
  int minute;
  int second;
}


//---------- Il codice seguente definisce la classe Q
class Q
{

public:
  int Q(int);
  void setQ(int);
  void printQ();
  int operateQ(int);

private:
  int qData;

};


//--------- Il codice seguente e` un'altra versione della definizione della classe Q
class Q
{

public:
  Q(int);
  void setQ(int);
  void printQ();
  int operateQ(int);

private:
  int qData = 1;
};


//--------- Il codice seguente definisce il metodo setQ dell'ultima classe Q definita. 

void setQ(int input)
{
  qData = input;
}
