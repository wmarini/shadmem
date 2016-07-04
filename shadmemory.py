"""Shared Memory for ShadMem program"""

class ShadBaseSharedMemory(Exception):
    """Base exception class for Shared Memory."""
    pass

class ShadSharedMemory(ShadBaseSharedMemory):
    """Shared memory class"""
    errno = None

    def __init__(self,shrdmm=None,verbse=False):
        self.sharedmemory = shrdmm
        self.sharedmemoryctx = None
        self.verbose = verbse

    def __str__(self):
        return str(self.sharedmemoryctx)

    def __repr__(self):
        return "Shared Memory"

    def open(self):
        if self.verbose:
            print('[+] Opening Shared Memory')

    def close(self):
        if self.verbose:
            print('[+] Closing Shared Memory')

    def read(self,cmd):
        pass
