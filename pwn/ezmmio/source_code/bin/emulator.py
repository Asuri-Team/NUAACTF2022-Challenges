from qiling import Qiling
from qiling.extensions.nuaactf.linux import nuaa_ctf_device
from qiling.const import QL_VERBOSE
from unicorn.x86_const import UC_X86_INS_SYSCALL

def patch_syscall(ql:Qiling, intno=None):
    if intno == 0:
        return 
    print('Dear, can\'t do more than read')
    exit(1)

def main():
    PWN_ELF_PATH = '/home/ctf/shellcode'
    ql = Qiling([PWN_ELF_PATH], "/src/qiling-1.4.4/examples/rootfs/x8664_linux", archtype="x8664", ostype="linux", 
                    env=nuaa_ctf_device, verbose=QL_VERBOSE.DISABLED)
    ql.hw.create('executor')
    ql.hw.setup_mmio(0xdeadb000, 0x1000, info=f'executor')
    
    ql.hook_insn(patch_syscall, UC_X86_INS_SYSCALL, begin=0xdeadbeef000, end=0xdeadbef0000)
    
    ql.run()

if __name__ == '__main__':
    exit(main())
