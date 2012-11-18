/**
 * @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include <QApplication>
#include <QGraphicsScene>
#include <QGraphicsItem>
#include <QGraphicsItemAnimation>
#include <QGraphicsView>
#include <QTimeLine>
#include <QGLWidget>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

    /* A surface to manage various 2D graphical items; it has algorithms for animations and collision detection */
    QGraphicsScene* scene = new QGraphicsScene();

    /* A scene contains instances of QGraphicsItem, such as lines, rectangles, text, or custom items */
    QGraphicsItem* hello = scene->addText("Hello, world!");
    hello->setPos(0, -100);

    /* QGraphicsView can either visualize the whole scene, or zoom in and view only parts of the scene */
    QGraphicsView* view = new QGraphicsView(scene);
    view->setSceneRect(0, 0, 800, 600);
    view->fitInView(0, 0, 800, 600);

    /* Use OpenGL acceleration, if available */
    view->setViewport(new QGLWidget());
    view->show();

    QTimeLine *timer = new QTimeLine(5000);
    timer->setLoopCount(0);
    timer->setCurveShape(QTimeLine::LinearCurve);

    QGraphicsItemAnimation *animation =
        new QGraphicsItemAnimation();
    animation->setItem(hello);

    animation->setPosAt(0, QPointF(0, 0));
    animation->setRotationAt(0, 0);
    animation->setScaleAt(0, 0, 0);

    animation->setPosAt(0.5, QPointF(360, 360));
    animation->setRotationAt(0.5, 360);
    animation->setScaleAt(0.5, 4, 4);

    animation->setPosAt(1, QPointF(0, 0));
    animation->setRotationAt(1, 0);
    animation->setScaleAt(1, 0, 0);

    animation->setTimeLine(timer);

    timer->start();

    return a.exec();
}
