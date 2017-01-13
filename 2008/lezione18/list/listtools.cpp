//This is the implementation file listtools.cpp. This file contains 
//function definitions for the functions declared in listtools.h.
#include <cstddef>
#include "listtools.h"

namespace LinkedListSavitch
{
    template<class T>
    void headInsert(Node<T>*& head, const T& theData)
    {
        head = new Node<T>(theData, head);
    }

    template<class T>
    void insert(Node<T>* afterMe, const T& theData)
    {
        afterMe->setLink(new Node<T>(theData, afterMe->getLink( )));
    }

    template<class T>
    void deleteNode(Node<T>* before)
    {
        Node<T> *discard;
        discard = before->getLink( );
        before->setLink(discard->getLink( ));
        delete discard;
    }

    template<class T>
    void deleteFirstNode(Node<T>*& head)
    {
        Node<T> *discard;
        discard = head;
        head = head->getLink( );
        delete discard;
    }

    //Uses cstddef:
    template<class T>
    Node<T>* search(Node<T>* head, const T& target)
    {
        Node<T>* here = head;

        if (here == NULL) //if empty list
        {
            return NULL;
        }
        else
        {
            while (here->getData( ) != target && here->getLink( ) != NULL)
                here = here->getLink( );

            if (here->getData( ) == target)
                return here;
            else
                return NULL;
        }
    }

}//LinkedListSavitch