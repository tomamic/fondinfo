TEMPLATE = app
CONFIG += console
CONFIG += c++11
CONFIG -= app_bundle
CONFIG -= qt

SOURCES += main.cpp \
    node.cpp \
    file.cpp \
    folder.cpp

HEADERS += \
    node.h \
    file.h \
    folder.h

