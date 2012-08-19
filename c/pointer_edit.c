// Showing that we can edit memory with pointers

#include<stdio.h>

int main() {

    int number = 5;
    int *ptr = &number;

    *ptr = 10;

    printf("The value of number is: %d\n", number);

    return 0;
}
