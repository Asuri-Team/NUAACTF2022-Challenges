# include <unistd.h>
# include <sys/mman.h>

int main() {
    char *shellcode = mmap(0xdeadbeef000, 0x1000, PROT_EXEC | PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    read(0, shellcode, 0x1000);
    ((void (*) (void))(shellcode))();
    return 0; 
}