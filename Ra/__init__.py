#!/usr/bin/env -S python

from .modules.argpaser import args

if args.battery:
    print("79%")

# if args.connected: 
#     print("Hussein Mukhtar         90%")

# if args.bright: 
#     print(args.bright)


def main():
    Core(args)    #! Make it 