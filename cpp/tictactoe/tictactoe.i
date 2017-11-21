%module tictactoe

%include <std_string.i>

%{
/* Includes the header in the wrapper code */

#include "tictactoe.h"

%}

/* Parse the header file to generate wrappers */

%include "tictactoe.h"
