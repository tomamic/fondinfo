all: setTest

setTest: main.o ElementSet.o 
	g++ -Wall --pedantic -o setTest main.o ElementSet.o

main.o: main.cpp ElementSet.h
	g++ -Wall --pedantic -c main.cpp

ElementSet.o: ElementSet.cpp ElementSet.h
	g++ -Wall --pedantic -c ElementSet.cpp

clean:
	rm -f *.o setTest
