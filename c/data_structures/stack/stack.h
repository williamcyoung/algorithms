#ifndef __STACK__
#define __STACK__

// initializes the stack with 10 element capacity
void initStack();

// push: pushes the argument onto the stack
void push(void *object);

/* 
    pop: pops the top element of the stack from the stack
    assumes the stack is not empty.
*/
void *pop();

// size: gets the number of elements in the stack
int size();

// isEmpty(): returns 1 if stack is empty; otherwise 0
int isEmpty();

// top: returns the top element from the stack without removing it
void *top();

#endif