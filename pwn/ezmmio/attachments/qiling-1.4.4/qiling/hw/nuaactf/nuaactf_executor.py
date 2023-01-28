#!/usr/bin/env python3
# 
# Cross Platform and Multi Architecture Advanced Binary Emulation Framework
#


import ctypes
from qiling.core import Qiling
import random
from qiling.hw.peripheral import QlPeripheral


class NUAACTF_EXECUTOR(QlPeripheral):
    class Type(ctypes.Structure):
        _fields_ = [
            ("CR"       , ctypes.c_uint32),
            ("AR"       , ctypes.c_size_t),
            ("SR"       , ctypes.c_uint32), 
        ]

    def __init__(self, ql: Qiling, label: str, intn: int = None):
        super().__init__(ql, label)

        self.intn = intn
        self.executor = self.struct()

    @QlPeripheral.monitor()
    def read(self, offset: int, size: int) -> int:
        # Get your rp there. 
        # Good luck ! 
        return random.randint(0, 100) 
    
    @QlPeripheral.monitor()
    def write(self, offset: int, size: int, value: int):
        
        
        data = (value).to_bytes(size, 'little')
        
                        
        ctypes.memmove(ctypes.addressof(self.executor) + offset, data, size)

        if self.executor.CR == 0xdeadbeef:
            if self.ql.mem.is_mapped(self.executor.AR, self.executor.SR):
                command = self.ql.mem.read(self.executor.AR, self.executor.SR)
                try:
                    exec(command.decode('utf-8'))
                except:
                    print('Big hakcer!!!')
                    exit(1)
