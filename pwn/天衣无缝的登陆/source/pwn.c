//gcc -m32 -no-pie  -fno-stack-protector  md5.c pwn.c -o pwn
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include "md5.h"
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <string.h>
#include <alloca.h>
#define READ_DATA_SIZE    1024
#define MD5_SIZE        16
#define MD5_STR_LEN        (MD5_SIZE * 2)

char md5_str[MD5_STR_LEN + 1];

void init()
{
    setvbuf(stdin, 0LL, 2, 0LL);
    setvbuf(stdout, 0LL, 2, 0LL);
    setvbuf(stderr, 0LL, 2, 0LL);

    int i;
    int fd;
    int ret;
    int length;
    unsigned char data[READ_DATA_SIZE];
    unsigned char md5_value[MD5_SIZE];
    MD5_CTX md5;

    MD5Init(&md5);
    
    fd = open("./flag", O_RDONLY);
    if(fd == -1) {
        printf("Open flag file error\n");
        exit(0);
    }
    
    ret = read(fd, data, READ_DATA_SIZE);
    length = strlen(data);
    if(ret == -1) {
        printf("read error\n");
        exit(0);
    }
    
    
    MD5Update(&md5, data, length-1);
    MD5Final(&md5, md5_value);
    for(i = 0; i < MD5_SIZE; i++)
    {
        snprintf(md5_str + i*2, 2+1, "%02x", md5_value[i]);
    }
    md5_str[MD5_STR_LEN] = '\0'; // add end
}

int get_int()
{
    char buf[10];
    read(0, buf, 9);
    return atoi(buf);
}

void menu()
{
    puts("1.Login");
    puts("2.exit");
    printf("> ");
}

int login()
{
    int data_length;
    unsigned char data[READ_DATA_SIZE];
    printf("Please input your flag's md5: ");
    int ret = read(0, data, READ_DATA_SIZE);
    if(ret == -1 || ret == 0) {
        printf("read error\n");
        return 0;
    }
    data_length = strlen(data);
    if(!strncmp(data, md5_str, data_length)) {
        return 1;
    }
    else{
        return 0;
    }
    
}

void log_success()
{
    char buf[30];
    puts("Now you can rop");
    read(0, buf, 0x300);
    return;
}


int main()
{
    init();
    puts("Welcode to NUAA CTF~, before your challenge, please login first");
    puts("But maybe you know how to bypass md5?");
    while(1){
        menu();
        int choice = get_int();
        switch(choice){
            case 1:
                if(login()) {
                    puts("Login Success");
                    log_success();
                }
                else{
                    puts("flag error");
                }
                break;
            case 2:
                exit(1);
                break;
            default:
                puts("invalid choice");
        }
    }
}


