QT       += core
TARGET   = reverse-server
TEMPLATE = app
CONFIG   += console

SOURCES += main.cpp

LIBS += -L/usr/lib/ -lboost_system -lboost_thread
QMAKE_CXXFLAGS += -std=c++0x
