#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/*
 * main - checks the code
 * b: binary string
 * length: length of the binary string
 * result: the converted binary number
 * Return:result and 0 when b is NULL
 */
unsigned int binary_to_uint(const char *b)
{
int a;
unsigned int result = 0;
int length = strlen("b");
	if (b == NULL){
	printf("Empty string\n");
	return 0;
	}
		for (a = 0; a < length; a++){
		if (b[a] == '0'){
		result = (result << 1);
		}
	else if (b[a] == '1'){
	result = (result << 1) | 1;
	}
	else{
	printf("Invalid string!\n");
	return 0;
	}
		}
return result;
}

