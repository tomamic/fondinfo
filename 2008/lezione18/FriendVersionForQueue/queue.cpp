

//This is the implementation file queue.cpp.
//This is the implementation of the template class Queue.
//The interface for the template class Queue is in the header file queue.h.

#include <iostream>
#include <cstdlib>
#include <cstddef>
#include "queue.h"
using std::cout;


namespace QueueSavitch
{

//Uses cstddef:
template<class T>
Queue<T>::Queue( ) : front(NULL), back(NULL)
{
    //Intentionally empty.
}

//Uses cstddef:
template<class T>
bool Queue<T>::isEmpty( ) const
{
    return (back == NULL);//front == NULL would also work
}

    template<class T> //Uses cstddef:
    void Queue<T>::add(T item)
    {
       if (isEmpty( ))
           front = back = new Node<T>(item, NULL);
        else
       {
           back->link = new Node<T>(item, NULL);
           back = back->link;
       }
    }

    template<class T> //Uses cstdlib and iostream:
    T Queue<T>::remove( )
    {
        if (isEmpty( ))
        {
            cout << "Error: Removing an item from an empty queue.\n";
            exit(1);
        }

        T result = front->data;

        Node<T> *discard;
        discard = front;
        front = front->link;
        if (front == NULL) //if you removed the last node
            back = NULL;

        delete discard;
        return result;
    }

template<class T>
Queue<T>::~Queue( )
{
    T next;
    while (! isEmpty( ))
       next = remove( );//remove calls delete.
}

//Uses cstddef:
template<class T>
Queue<T>::Queue(const Queue<T>& aQueue)
{
    if (aQueue.isEmpty( ))
        front = back = NULL;
    else
    {
        Node<T> *temp = aQueue.front;//temp moves
        //through the nodes from front to back of aQueue.

        back = new Node<T>(temp->data, NULL);
        front = back;
        //First node created and filled with data.
        //New nodes are now added AFTER this first node.

        temp = temp->link;//temp now points to second
                //node or NULL if there is no second node.

        while (temp != NULL)
        {
            back->link = new Node<T>(temp->data, NULL);
            back = back->link;
            temp = temp->link;

        }
        //back->link == NULL
    }
}

//Uses cstddef:
template<class T>
Queue<T>& Queue<T>::operator =(const Queue<T>& rightSide)
{
    if (front == rightSide.front)//if the queues are the same
        return *this;
    else //send left side back to freestore
    {
        T next;
        while (! isEmpty( ))
            next = remove( );//remove calls delete.
    }

    if (rightSide.isEmpty( ))
    {
        front = back = NULL;
        return *this;
    }
    else
    {
        Node<T> *temp = rightSide.front;//temp moves 
          //through the nodes from front to back of rightSide.

        back = new Node<T>(temp->data, NULL);
        front = back;
        //First node created and filled with data.
        //New nodes are now added AFTER this first node.

        temp = temp->link;//temp now points to second
                   //node or NULL if there is no second node.

        while (temp != NULL)
        {
            back->link =
                     new Node<T>(temp->data, NULL);
            back = back->link;
            temp = temp->link;
        }
        //back->link == NULL;

        return *this;
    }
}

}//QueueSavitch