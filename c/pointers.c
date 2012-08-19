// Just a program about pointers

#include<stdio.h>

int main() {

    // Make a value and a pointer that points to it
    int my_int = 1;
    int *ptr = &my_int;

    // Print out information about the variables
    printf("The character is: %d\n", my_int);
    printf("The address of the character is: %p\n", &my_int);
    printf("The address the pointer points to is: %p\n", ptr);
    printf("The value the pointer is pointing to is: %d\n", *ptr);

    return 0;
}
