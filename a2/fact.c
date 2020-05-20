#include <stdio.h>
#include <limits.h>

int fact(int n) {
	if(n < 0)
		return INT_MAX;
	
	if(n == 0)
		return 1;
	
	return (n * fact(n - 1));
}
int main() {
	int n = 3;
	fact(n);
	return 0;
}

