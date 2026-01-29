#!/usr/bin/env python3
from app import run

import sys

__version__ = '0.4'
__author__ = 'Alexei Metlitski'

def main():
    code = run(sys.argv);
    sys.exit(code)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('[!] Exiting... (SIGINT)')
        sys.exit(1)
    except EOFError:
        print("[!] Exiting... (EOF)")
        sys.exit(1)
