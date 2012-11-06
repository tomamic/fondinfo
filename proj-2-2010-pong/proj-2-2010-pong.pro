TEMPLATE = app
CONFIG += console
QT += core gui

SOURCES += main.cpp\
    actor.cpp \
    loader.cpp \
    game.cpp \
    gamegui.cpp \
    ball.cpp \
    paddle.cpp \
    autopaddle.cpp

HEADERS  += actor.h \
    loader.h \
    game.h \
    gamegui.h \
    ball.h \
    paddle.h \
    autopaddle.h

OTHER_FILES += pong-1.dat

RESOURCES += pong.qrc

TRANSLATIONS = pong_it.ts
