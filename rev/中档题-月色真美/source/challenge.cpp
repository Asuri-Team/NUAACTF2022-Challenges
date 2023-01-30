#include<bits/stdc++.h>
using namespace std;
char input[21];
void init(unsigned char *s,unsigned char *key,int len){
	int i = 0,j = 0;
	char k[256] = {0};
	unsigned char tmp = 0;
	for (i=0;i < 256;i++) {
		s[i] = i;
		k[i] = key[i%len];
	}
	for (i=0;i < 256;i++) {
		j = (j + s[i] + k[i]) % 256;
		tmp = s[i];
		s[i] = s[j];
		s[j] = tmp;
	}
}

void crypt(unsigned char *s,unsigned char *str,int len){
	int i=0,j=0,t=0;
	unsigned long k=0;
	unsigned char tmp;
	for(k=0;k<len;k++){
		i=(i+1)%256;
		j=(j+s[i])%256;
		tmp=s[i];
		s[i]=s[j];
		s[j]=tmp;
		t=(s[i]+s[j])%256;
		str[k]^=s[t];
	}
}

int main(){
	
	
	unsigned char s[256];
	char key[]="AttackonTitan";
	init(s,(unsigned char *)key,strlen(key));
//	char m[]="0704Aremy3weeTe3T0ne";
	printf("Welcome!\n");
	printf("Guess what the title means?\n");
	printf("input your str:");
	scanf("%s",input);
	crypt(s,(unsigned char *)input,strlen(input));
//	for(int i=0;i<20;i++){
//		printf("%d ",input[i]);
//	}cout<<endl;
	char s2[]={71,-15,64,-33,-100,45,108,-99,-120,-53,111,46,68,-60,-112,-55,-31,96,71,111};
	for(int i=0;i<20;i++){
		if(input[i]!=s2[i]){
			printf("Wrong!\n");
			return 0;
		}
	}
	printf("Right!hhhh\n");
	printf("ÇëÄã³Ô¹·Á¸\n");
	init(s,(unsigned char *)key,strlen(key));
	crypt(s,(unsigned char *)input,strlen(input));
	printf("NUAACTF{%s}",input);
	return 0;
}
