#include <stdio.h>
#include <omp.h>

int main(){

	int steps;	// number of sections we are going to divide the graph into
	
	printf("Enter number of steps : ");
	scanf("%d", &steps);

	double width = (double) 1/steps;	// the width of each section
	double pi = 0;
	double x;

	#pragma omp parallel for	
	for(int i=1; i<steps; i++){
		x = (double) i * width;	// the value if x at the end of ith section
		pi += width * (4/(1+(0.25*x*x)));	// add area of section to pi
	}


	printf("%f\n", pi);

	return 0;
}
