import contextlib
import os

try:
    os.remove('somefile.tmp')
except FileNotFoundError:
    pass

with contextlib.suppress(FileNotFoundError):
    os.remove('somefile.tmp')