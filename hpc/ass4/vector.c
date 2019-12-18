#include <stdio.h>
#include <omp.h>

int main()
{

    FILE *file1 = fopen("input1.txt", "r");
    FILE *file2 = fopen("input2.txt", "r");
    FILE *op = fopen("output.txt", "w");

    long long int arr1[100], arr2[100];

#pragma omp parallel sections
    {
#pragma omp section
        {
            for (int i = 0; i < 100; i++)
            {
                fscanf(file1, "%lld", &arr1[i]);
            }
        }
#pragma omp section
        {
            for (int i = 0; i < 100; i++)
            {
                fscanf(file2, "%lld", &arr2[i]);
            }
        }
    }

    fclose(file1);
    fclose(file2);

    long long int sum[100];

#pragma omp parallel for
    for (int i = 0; i < 100; i++)
    {
        sum[i] = arr1[i] + arr2[i];
    }

    for (int i = 0; i < 100; i++)
    {
        fprintf(op, "%d ", sum[i]);
    }

    return 0;
}