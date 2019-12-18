#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <omp.h>

void generate(long long int size)
{

    FILE *file1 = fopen("input1.txt", "w");
    FILE *file2 = fopen("input2.txt", "w");

    for (long long int i = 0; i < size; i++)
    {
        fprintf(file1, "%lld ", rand());
    }
    for (long long int i = 0; i < size; i++)
    {
        fprintf(file2, "%lld ", rand());
    }

    fclose(file1);
    fclose(file2);
}

void read(FILE *file, long long int size, long long int *arr)
{
    for (int i = 0; i < size; i++)
    {
        fscanf(file, "%lld", &arr[i]);
    }
}

int main()
{

    long long int size;
    printf("Enter size of arrays to be generated : ");
    scanf("%lld", &size);

    generate(size);

    FILE *file1 = fopen("input1.txt", "r");
    FILE *file2 = fopen("input2.txt", "r");
    FILE *op = fopen("output.txt", "w");

    long long int arr1[size], arr2[size], sum[size];

    #pragma omp parallel sections
    {
        #pragma omp section
        {
            read(file1, size, arr1);
        }
        #pragma omp section
        {
            read(file2, size, arr2);
        }
    }

    fclose(file1);
    fclose(file2);

    #pragma omp parallel for
    for (long long int i = 0; i < size; i++)
    {
        sum[i] = arr1[i] + arr2[i];
    }

    for (long long int i = 0; i < size; i++)
    {
        fprintf(op, "%lld ", sum[i]);
    }

    return 0;
}