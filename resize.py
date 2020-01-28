import platform
import os
import sys


def resize_screen(x, y):
    clientos = platform.system()
    if clientos == 'Windows':
        os.system("mode {rows},{columns}".format(rows=x,columns=y))
    elif clientos == 'Linux' or clientos == 'Darwin':
        sys.stdout.write("\x1b[8;{columns};{rows}t".format(rows=x,columns=y))
    elif clientos.startswith('CYGWIN'):
        os.system("echo -ne '\e[8;{columns};{rows}t'".format(rows=x,columns=y))
