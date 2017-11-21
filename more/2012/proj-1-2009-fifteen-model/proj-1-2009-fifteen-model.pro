TEMPLATE = app
QT += core gui
QMAKE_CXXFLAGS += -std=c++11

SOURCES += main.cpp \
    fifteengui.cpp \
    fifteenmodel.cpp \
    fifteenpuzzle.cpp

HEADERS += fifteengui.h \
    fifteenmodel.h \
    fifteenpuzzle.h

TRANSLATIONS = fifteen_it.ts

RESOURCES += fifteen.qrc


