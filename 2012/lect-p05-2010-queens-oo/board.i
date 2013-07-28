%module board

%include "std_string.i"

%{
/* Includes the header in the wrapper code */

#include "board.h"

%}

/* Parse the header file to generate wrappers */

%include "board.h"
