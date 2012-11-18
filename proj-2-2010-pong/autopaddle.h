/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
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
