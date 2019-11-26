#include <stdio.h>
#include <omp.h>

int main(){

	int size;	// size of array to be sorted
	float temp;	// for swapping purpose
	printf("Enter size : ");
	scanf("%d", &size);

	float arr[size];
	// generate the array
	#pragma omp for
	for(int i=0; i<size; i++){
		arr[i] = size-i;
	}

	double start = omp_get_wtime();	// record start time

	// use bubble sort
	for(int i=0; i<size; i++){

		#pragma omp for
		for(int j=0; j<size-1; j+=2){	// compare even positioned elements
			if(arr[j]>arr[j+1]){
				// swap
				temp = arr[j];
				arr[j] = arr[j+1];
				arr[j+1] = temp;
			}
		}

		#pragma omp for
                for(int j=1; j<size-1; j+=2){        // compare odd positioned elements
                        if(arr[j]>arr[j+1]){
				// swap
                                temp = arr[j];
                                arr[j] = arr[j+1];
                                arr[j+1] = temp;
                        }
                }

	}

        // print execution time
        printf("\nTime = %f\n", (omp_get_wtime() - start));

}
