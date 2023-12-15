#include <stdio.h>

/*
 * main - checkss the code
 * Return: Always 0
 */

void print_binary(unsigned long int n){
int Bitnum = sizeof(n) * 8;
int j;
	for(j = Bitnum - 1; j >= 0; j--){
		int bit = (n >> 1) & 1;
	printf("%d\n", bit);
	}
printf("\n");
}
