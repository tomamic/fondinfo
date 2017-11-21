//This is the header file queue.h. This is the interface for the class Queue,
//which is a template class for a queue of items of type T, including iterators.
#ifndef QUEUE_H
#define QUEUE_H
#include "iterator.h"
using namespace ListNodeSavitch;

namespace QueueSavitch
{
    template<class T>
    class Queue
    {
    public:
        typedef ListIterator<T> Iterator;

        Queue( );
        Queue(const Queue<T>& aQueue);
        Queue<T>& operator =(const Queue<T>& rightSide);
        virtual ~Queue( );
        void add(T item);
        T remove( );
        bool isEmpty( ) const;

        Iterator begin( ) const { return Iterator(front); }
        Iterator end( ) const { return Iterator( ); }
        //The end iterator has end( ).current == NULL.
        //Note that you cannot dereference this iterator.
    private:
        Node<T> *front;//Points to the head of a linked list. 
                       //Items are removed at the head
        Node<T> *back;//Points to the node at the other end of the linked list.
                      //Items are added at this end.
    };

}//QueueSavitch

#endif //QUEUE_H

