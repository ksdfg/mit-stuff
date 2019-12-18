#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <omp.h>

// function to randomly generate two input files
void generate(char* filename, long long int size)
{
    FILE *file = fopen(filename, "w");  // open input file

    // write random number into input files
    for (long long int i = 0; i < size; i++)
    {
        fprintf(file, "%lld ", rand());
    }

    fclose(file);   // close input files
}

// function to read numbers from a file to an array
void read(FILE *file, long long int size, long long int *arr)
{
    for (int i = 0; i < size; i++)
    {
        fscanf(file, "%lld", &arr[i]);  // read a long long int at a time
    }
}

int main()
{
    long long int size;     // total number of elements in each input file
    printf("Enter size of arrays to be generated : ");
    scanf("%lld", &size);

    // generate the input files
    #pragma omp parallel sections
    {
        #pragma omp section
        {
            generate("input1.txt", size);
        }
        #pragma omp section
        {
            generate("input2.txt", size);
        }
    }

    // open the input and output files
    FILE *file1 = fopen("input1.txt", "r");
    FILE *file2 = fopen("input2.txt", "r");
    FILE *op = fopen("output.txt", "w");

    long long int arr1[size], arr2[size], sum[size];    // arrays for both inputs and output


    /* PARALLEL EXECUTION */
    double start = omp_get_wtime();

    // read input from both files
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

    // store sum of both vectors into sum
    #pragma omp parallel for
    for (long long int i = 0; i < size; i++)
    {
        sum[i] = arr1[i] + arr2[i];
    }

    // write output to op file
    for (long long int i = 0; i < size; i++)
    {
        fprintf(op, "%lld ", sum[i]);
    }

    printf("Parallel : %f\n", omp_get_wtime() - start);
    /* END PARALLEL EXECUTION */


    /* SERIAL EXECUTION */
    start = omp_get_wtime();

    // read input from both files
    read(file1, size, arr1);
    read(file2, size, arr2);

    // store sum of both vectors into sum
    for (long long int i = 0; i < size; i++)
    {
        sum[i] = arr1[i] + arr2[i];
    }

    // write output to op file
    for (long long int i = 0; i < size; i++)
    {
        fprintf(op, "%lld ", sum[i]);
    }

    printf("Serial : %f\n", omp_get_wtime() - start);
    /* END SERIAL EXECUTION */

    // close both input files since their job is done
    fclose(file1);
    fclose(file2);

    return 0;
}