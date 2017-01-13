//This is the header file iterator.h. This is the interface for the class ListIterator,
//which is a template class for an iterator to use with linked lists of items of type T.
#ifndef ITERATOR_H
#define ITERATOR_H

namespace ListNodeSavitch
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
    class ListIterator
    {
    public:
        ListIterator( ) : current(NULL) {}

        ListIterator(Node<T>* initial) : current(initial) {}

        const T operator *( ) const { return current->getData( ); }
        //Precondition: Not equal to the default constructor object,
        //that is, current != NULL.
 
        ListIterator operator ++( ) //Prefix form
        {
            current = current->getLink( );
            return *this;
        }

        ListIterator operator ++(int) //Postfix form
        {
            ListIterator startVersion(current);
            current = current->getLink( );
            return startVersion;
        }

        bool operator ==(const ListIterator& rightSide) const
        { return (current == rightSide.current); }
 
        bool operator !=(const ListIterator& rightSide) const
        { return (current != rightSide.current); }
 
        //The default assignment operator and copy constructor 
         //should work correctly for ListIterator,
    private:
        Node<T> *current;
    };

}//ListNodeSavitch

#endif //ITERATOR_H

