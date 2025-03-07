import ctypes

class MemoryPool:
    def __init__(self, size):
        self.pool = (ctypes.c_char * size)()
        self.offset = 0

    def allocate(self, size):
        if self.offset + size > len(self.pool):
            raise MemoryError("Out of memory!")
        ptr = ctypes.addressof(self.pool) + self.offset
        self.offset += size
        return ptr
