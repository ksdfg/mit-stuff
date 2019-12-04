#include <stdio.h>
#include <omp.h>

int main(){

    FILE* file1 = fopen("input1.txt", "r");
    FILE* file2 = fopen("input2.txt", "r");

    long long int n1, n2;

    #pragma omp parallel sections
    {
        #pragma omp section
        {
            scanf(file1, "%lld", &n1);
        }
        #pragma omp section
        {
            scanf(file1, "%lld", &n2);
        }
    }

    FILE* op = fopen('output.txt', 'w');
    fprintf(op, "%lld", (n1+n2));

    return 0;
}