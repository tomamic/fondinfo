/**
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - <tomamic@ce.unipr.it> - 2010
 *
 * This software is free: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#ifndef AUTOPADDLE_H
#define AUTOPADDLE_H

#include "paddle.h"

class AutoPaddle : public Paddle
{
public:
    AutoPaddle(Game* game, int y, int x, int id);
    void move();
};

#endif // AUTOPADDLE_H
