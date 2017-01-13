all: listTest

listTest: main.o ElementList.o 
	g++ -Wall --pedantic -o listTest main.o ElementList.o

main.o: main.cpp ElementList.h
	g++ -Wall --pedantic -c main.cpp

ElementList.o: ElementList.cpp ElementList.h
	g++ -Wall --pedantic -c ElementList.cpp

clean:
	rm -f *.o listTest
