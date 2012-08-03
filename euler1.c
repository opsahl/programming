#include <stdio.h>

// Declaration
int solve(int max);

int solve(int max){
    int sum = 0;
    int i = 0;
    for(i = 0; i < max; i++){
        if(i % 3 == 0 || i % 5 == 0){
            sum += i;
        }
    }

    return sum;
}

int main(int argc, char *argv[]){
    printf("%d\n", solve(10));
    printf("%d\n", solve(1000));
    return 0;
}
