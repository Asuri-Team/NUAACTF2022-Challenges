#include<bits/stdc++.h>
using namespace std;

char s[31];
int v1,v2;
void judge1(){
	char a[]="We1c0me_t0_";
	for(int i=0;i<strlen(a);i++){
		if(a[i]!=s[i])v1=0;
	}
}

void judge2(){
	char a[]="d1r0w_esrever_eht";
	int cnt=strlen(s)-1;
	for(int i=0;i<strlen(a);i++){		
		if(a[i]!=s[cnt])v2=0;
		cnt--;
	}
}

int main(){
	printf("Can you find where the flag is?\n");
	printf("Please input your flag:") ;
	scanf("%s",&s);
	v1=1,v2=1;
	judge1();
	judge2();
	if(v1&&v2){
		printf("WoW,you find it\n");
		printf("NUAACTF{%s}",s);
	}else printf("try again");
}
