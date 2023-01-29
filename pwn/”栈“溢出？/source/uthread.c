/* uthread.c */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

struct context {
	unsigned long rsp;
	unsigned long rbp;
	unsigned long rip;
	unsigned long r12;
	unsigned long r13;
	unsigned long r14;
	unsigned long r15;
};

unsigned char *stack1, *stack2;
struct context *ctx1, *ctx2;


void schedule(struct context *prev, struct context *next)
{
	int ret;
	ret = save(prev);
	if (ret == 0) {
		restore(next);
	}
}

void func1()
{
	int i = 1;
	long long int length=0;
	char content[8];
	
	
	puts("len:");
	scanf("%lld",&length);
	//int len = (int)length;
	if(length > 16)
	{
		puts("too long!!!BYEBYE~");exit(0);
	}

	while (i++) {
		//printf("Bob  :%d\n", i);
		puts("Bob  :");
		putchar((i+33)%126);
		puts("    over");
		//sleep(1);
		if (i%3 == 0) {
			
			puts("input:");
			read(0,content,(int)length);
			//printf("content:%s\n",content);
			puts("content:");
			puts(content);
			schedule(ctx1, ctx2);
		}
		
	}
}

void func2()
{
	int i = 0xffff;
	long long int length=0;
	char content[8];
	
	puts("len:");
	scanf("%lld",&length);
	//int len = (int)length;
	if(length > 16)
	{
		puts("too long!!!BYEBYE~");exit(0);
	}
	while (i--) {
		puts("Alice  :");
		putchar((i+33)%126);
		//printf("Alice  :%d\n", i);
		puts("    over");
		puts("input:");
		read(0,content,(int)length);
		//printf("content:%s\n",content);			
		puts("content:");
		puts(content);
		
		//sleep(1);
		if (i%3 == 0) {

			schedule(ctx2, ctx1);
			
		}
	}
}

int main()
{
	setvbuf(stdin, 0LL, 2, 0LL);
	setvbuf(stdout, 0LL, 2, 0LL);
	setvbuf(stderr, 0LL, 2, 0LL);
	//init();
	int i, j, k;
	char tmp[8];

	stack1 = (unsigned char *)malloc(4096);
	stack2 = (unsigned char *)malloc(4096);
	ctx1 = (struct context *)malloc(sizeof(struct context));
	ctx2 = (struct context *)malloc(sizeof(struct context));

	memset(ctx1, 0, sizeof(struct context));
	memset(ctx2, 0, sizeof(struct context));

	i =save(ctx1);
	j =save(ctx2);

	
	ctx1->rip = &func1;

	ctx1->rsp = ctx1->rbp = stack1+4000;
	ctx2->rip = &func2;
	ctx2->rsp = ctx2->rbp = stack2+4000;

	puts("It's time to play !!!");
	puts("when it's your turn,Be brave enough to say what you want to say!");
	puts("Are you ready?");

	read(0,tmp,0x200);
	puts("detect:xixi,you can not hack me !Beacaues I'm protected by my best friend ---- canary");
	
	k = restore(ctx1);
	
	return 0;
}
