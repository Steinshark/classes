long fibonacci(long N){
	if(N <= 1)
		return N;
	else
		return fibonacci(N-1) + fibonacci(N-2);
}



//build stack
add	sp, sp, 32		//32 for now
stur lr [sp, 0]
stur x19 [sp, 8]	//save x19 for N

mov x19, x1				//N is saved

//if N <= 1
subs x9, x19, 1		//check
 
