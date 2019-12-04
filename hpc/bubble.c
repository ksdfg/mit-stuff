#include <stdio.h>
#include <omp.h>

int main(){

	unsigned long long int size;	// size of arr_paray to be sorted
	unsigned long long int temp;	// for swapping purpose
	printf("Enter size : ");
	scanf("%llu", &size);

	unsigned long long int arr_par[size];
	unsigned long long int arr_ser[size];
	// generate the arr_paray
	#pragma omp for
	for(unsigned long long int i=0; i<size; i++){
		arr_par[i] = size-i;
		arr_ser[i] = size-i;
	}

	double start = omp_get_wtime();	// record start time

	// use bubble sort parallely
	for(unsigned long long int i=0; i<size; i++){

		#pragma omp for
		for(unsigned long long int j=0; j<size-1; j+=2){	// compare even positioned elements
			if(arr_par[j]>arr_par[j+1]){
				// swap
				temp = arr_par[j];
				arr_par[j] = arr_par[j+1];
				arr_par[j+1] = temp;
			}
		}

		#pragma omp for
        for(unsigned long long int j=1; j<size-1; j+=2){        // compare odd positioned elements
                if(arr_par[j]>arr_par[j+1]){
					// swap
					temp = arr_par[j];
					arr_par[j] = arr_par[j+1];
					arr_par[j+1] = temp;
                }
        }

	}

    // print execution time
    printf("\nTime for parallel execution = %f\n", (omp_get_wtime() - start));

	start = omp_get_wtime();	//record start time

	// use bubble sort serially
	for(unsigned long long int i=0; i<size; i++){
		for(unsigned long long int j=0; j<size-i-1; j++){
			if(arr_par[j]>arr_par[j+1]){
				// swap
				temp = arr_par[j];
				arr_par[j] = arr_par[j+1];
				arr_par[j+1] = temp;
			}
		}
	}

    // print execution time
    printf("\nTime for serial execution = %f\n", (omp_get_wtime() - start));

}
