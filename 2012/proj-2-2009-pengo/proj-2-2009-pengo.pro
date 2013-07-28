TEMPLATE = app
CONFIG += console
QT += core gui

SOURCES += main.cpp \
    penguin.cpp \
    ice.cpp \
    ghost.cpp \
    actor.cpp \
    loader.cpp \
    game.cpp \
    gamegui.cpp

HEADERS += pengogui.h \
    penguin.h \
    level.h \
    ice.h \
    ghost.h \
    actor.h \
    loader.h \
    game.h \
    gamegui.h

OTHER_FILES += pengo-1.dat

RESOURCES += pengo.qrc

TRANSLATIONS = pengo_it.ts \
               pengo_fr.ts

