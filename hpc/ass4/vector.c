#include <stdio.h>
#include <omp.h>

int main(){

    FILE* file1 = fopen("input1.txt", "r");
    FILE* file2 = fopen("input2.txt", "r");

    long long int arr1[100], arr2[100];

    #pragma omp parallel sections
    {
        #pragma omp section
        {
            for(int i=0; i<100; i++){
                scanf(file1, "%lld", &arr1[i]);
            }
        }
        #pragma omp section
        {
            for(int i=0; i<100; i++){
                scanf(file1, "%lld", &arr2[i]);
            }
        }
    }

    long long int sum[100];

    return 0;
}