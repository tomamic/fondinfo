QT       += core
TARGET   = 2011-reverse-server
TEMPLATE = app
CONFIG   += console

SOURCES += main.cpp

LIBS += -L/usr/lib/ -lboost_system
QMAKE_CXXFLAGS += -std=c++0x
