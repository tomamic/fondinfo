TEMPLATE = app
CONFIG += console
QT += core

SOURCES += main.cpp

LIBS += -L/usr/lib/ -lboost_system -lboost_thread
QMAKE_CXXFLAGS += -std=c++11
