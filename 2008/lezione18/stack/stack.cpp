//This is the implementation file stack.cpp.
//This is the implementation of the template class Stack.
//The interface for the template class Stack is in the header file stack.h.

#include <iostream>
#include <cstdlib>
#include <cstddef>
#include "stack.h"
using std::cout;


namespace StackSavitch
{
 
   //Uses cstddef:
    template<class T>
    Stack<T>::Stack( ) : top(NULL)
    {
        //Intentionally empty
    }

    //Uses cstddef:
    template<class T>
    Stack<T>::Stack(const Stack<T>& aStack)
    {
        if (aStack.isEmpty( ))
            top = NULL;
        else
        {
            Node<T> *temp = aStack.top;//temp moves
                //through the nodes from top to bottom of aStack.
            Node<T> *end;//Points to end of the new stack.

            end = new Node<T>(temp->getData( ), NULL);
            top = end;
            //First node created and filled with data.
            //New nodes are now added AFTER this first node.
        
            temp = temp->getLink( );//move temp to second node
                    //or NULL if there is no second node.
            while (temp != NULL)
            {
                end->setLink(
                          new Node<T>(temp->getData( ), NULL));
                temp = temp->getLink( );
                end = end->getLink( );
            }
        //end->link == NULL;
        }
    }

    template<class T>
    Stack<T>& Stack<T>::operator =(const Stack<T>& rightSide)
    {
        if (top == rightSide.top) //if two stacks are the same
            return *this;
        else //send left side back to freestore
        {
            T next;
            while (! isEmpty( ))
                next = pop( );//remove calls delete.
        }

        if (rightSide.isEmpty())
        {
            top = NULL;
            return *this;
        }
        else
        {
            Node<T> *temp = rightSide.top;//temp moves
                //through the nodes from front top to bottom of rightSide.

            Node<T> *end;//Points to end of the left side stack.
            end = new Node<T>(temp->getData( ), NULL);
            top = end;;
            //First node created and filled with data.
            //New nodes are now added AFTER this first node.

            temp = temp->getLink();//Move temp to second node
                     //or set to NULL if there is no second node.
           
            while (temp != NULL)
            {
                end->setLink(new Node<T>(temp->getData(), NULL));
                temp = temp->getLink();
                end = end->getLink();
            }
            //back->link == NULL;

            return *this;
        }
    }

    template<class T>
    Stack<T>::~Stack( )
    {
        T next;
        while (! isEmpty( ))
           next = pop( );//pop calls delete.
    }

    //Uses cstddef:
    template<class T>
    bool Stack<T>::isEmpty( ) const
    {
        return (top == NULL);
    }

    template<class T>
    void Stack<T>::push(T stackFrame)
    {
       top = new Node<T>(stackFrame, top);
    }

    //Uses cstdlib and iostream:
    template<class T>
    T Stack<T>::pop( )
    {
        if (isEmpty( ))
        {
            cout << "Error: popping an empty stack.\n";
            exit(1);
        }

        T result = top->getData( );

        Node<T> *discard;
        discard = top;
        top = top->getLink( );

        delete discard;

        return result;
    }

}//StackSavitch

 
