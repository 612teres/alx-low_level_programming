#include <stdio.h>

/*
 * main - checkss the code
 * Return: Always 0
 */

void print_binary(unsigned long int n){
int j;
	for(j = sizeof(n) * 8; j != -1; j--){
		int bit = (n >> 1) & 1;
	printf("%d\n", bit);
	}
printf("\n");
}
