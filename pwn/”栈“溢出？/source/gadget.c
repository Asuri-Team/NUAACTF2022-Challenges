#include <stdio.h>

void gad()
{
    __asm__ ("syscall   \n\t" 
             "pop %rdx  \n\t"
             "ret       \n\t"
             "pop %rdi \n\t"   
             "ret       \n\t"
             "pop %rsi \n\t"
             "ret       \n\t"
             "pop %rax \n\t"
             "ret       \n\t"
            );
}