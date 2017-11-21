TEMPLATE = app
CONFIG += console c++11
CONFIG -= app_bundle
CONFIG -= qt

SOURCES += main.cpp \
    literal.cpp \
    sum.cpp \
    product.cpp

HEADERS += \
    expression.h \
    literal.h \
    sum.h \
    product.h
