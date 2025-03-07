import ctypes
import threading

class MemoryPool:
    """A high-performance memory pool for efficient memory allocation."""
    
    def __init__(self, size: int = 8 * 1024 * 1024):
        """Initialize a memory pool of the given size (default: 8MB)."""
        self.pool = (ctypes.c_char * size)()  # Create a memory block
        self.offset = 0
        self.lock = threading.Lock()  # Thread-safe memory allocation
        self.size = size

    def allocate(self, size: int):
        """Allocate a block of memory from the pool."""
        with self.lock:
            if self.offset + size > self.size:
                raise MemoryError("Out of memory!")
            ptr = ctypes.addressof(self.pool) + self.offset
            self.offset += size
            return ptr

    def reset(self):
        """Reset the memory pool (free all allocated memory)."""
        with self.lock:
            self.offset = 0  # Simply reset the offset

# Global memory pool instance
mem_pool = MemoryPool()
