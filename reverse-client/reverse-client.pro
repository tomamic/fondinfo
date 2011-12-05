QT       += core
TARGET   = reverse-client
TEMPLATE = app
CONFIG   += console

SOURCES += main.cpp

LIBS += -L/usr/lib/ -lboost_system -lboost_thread
QMAKE_CXXFLAGS += -std=c++0x
