#include <cstddef>

class IntNode
{
public:
    IntNode( ){}
    IntNode(int theData, IntNode* theLink) 
            : data(theData), link(theLink){}
    IntNode* getLink( ) const { return link; }
    int getData( ) const { return data; }
    void setData(int theData) { data = theData; }
    void setLink(IntNode* pointer) { link = pointer; }
private:
    int data;
    IntNode *link;
};

typedef IntNode* IntNodePtr;


//Function to Add a Node at the Head of a Linked List

//Function Declaration

void headInsert(IntNodePtr& head, int theData);
//Precondition: The pointer variable head points to
//the head of a linked list.
//Postcondition: A new node containing theData
//has been added at the head of the linked list.

//Function Definition

void headInsert(IntNodePtr& head, int theData)
{
   head = new IntNode(theData, head);
}


//Function to Add a Node in the Middle of a Linked List

//Function Declaration

void insert(IntNodePtr afterMe, int theData);
//Precondition: afterMe points to a node in a linked list.
//Postcondition: A new node containing theData
//has been added after the node pointed to by afterMe.

//Function Definition

void insert(IntNodePtr afterMe, int theData)
{
    afterMe->setLink(new IntNode(theData, afterMe->getLink( )));
}


// Function to Locate a Node in a Linked List
// 
//Function Declaration

IntNodePtr search(IntNodePtr head, int target);
//Precondition: The pointer head points to the head of a 
//linked list. The pointer variable in the last node is NULL.
//If the list is empty, then head is NULL.
//Returns a pointer that points to the first node that contains the
//target. If no node contains the target, the function returns NULL.

//Function Definition

//Uses cstddef:
IntNodePtr search(IntNodePtr head, int target)
{
        IntNodePtr here = head;

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



