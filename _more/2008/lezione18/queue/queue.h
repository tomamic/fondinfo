
//This is the header file queue.h. This is the interface for the class Queue,
//which is a template class for a queue of items of type T.
#ifndef QUEUE_H
#define QUEUE_H

namespace QueueSavitch
{
    template<class T>
    class Node
    {
    public:
        Node(T theData, Node<T>* theLink) : data(theData), link(theLink){}
        Node<T>* getLink( ) const { return link; }
        const T getData( ) const { return data; }
        void setData(const T& theData) { data = theData; }
        void setLink(Node<T>* pointer) { link = pointer; }
    private:
        T data;
        Node<T> *link;
    };


    template<class T>
    class Queue
    {
    public:
        Queue( );
        //Initializes the object to an empty queue.

        Queue(const Queue<T>& aQueue);

        Queue<T>& operator =(const Queue<T>& rightSide);

        virtual ~Queue( );

        void add(T item);
        //Postcondition: item has been added to the back of the queue.

        T remove( );
        //Precondition: The queue is not empty.
        //Returns the item at the front of the queue
        //and removes that item from the queue.

        bool isEmpty( ) const;
        //Returns true if the queue is empty. Returns false otherwise.
    private:
        Node<T> *front;//Points to the head of a linked list. 
                       //Items are removed at the head
        Node<T> *back;//Points to the node at the other end of the linked list.
                      //Items are added at this end.
    };

}//QueueSavitch

#endif //QUEUE_H


