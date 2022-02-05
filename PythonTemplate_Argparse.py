import argparse
from ast import Global
import sys

GLOBALARGS=None

def ProccessCmdLineArgs():
    parser = argparse.ArgumentParser(description='PythonTemplate_Argparse')
    #required positional string argument
    parser.add_argument(    'PARAM1',
                            help='Parameter 1'
                        )
    #required positional int argument
    parser.add_argument(    'PARAM2',
                            help='Parameter 2',
                            type=int
                        )     
    # verbose options usually preceeded by double dash               
    parser.add_argument(    '--OPTION1',
                            action='store_true',
                            help='boolean'
                        )
    # short options usually preceeded by single dash
    parser.add_argument(    '-O2',
                            action='store_true',
                            help='O2 boolean'
                        )
    parser.add_argument(    '-v','--verbosity',
                            type=int, choices= {0,1,2},
                            help='short and verbose verbosity option of type int with limit of 0,1,2 as choices'
                        )
    # Parameter is now made to be required using required=True
    parser.add_argument(    '--file',
                            type=str,
                            required=True,
                            help='argument of type string'
                        )
    parser.add_argument(    '--values',
                            type=int,
                            nargs='+',  # Can also be an int to respresent limited amount of arguments to take
                            help='unlimited value input of type int'
                        )

    global GLOBALARGS  #required to modify GLOBALARGS (not required to read it)
    GLOBALARGS = parser.parse_args()


    if GLOBALARG.PARAM1=="INVALID" and GLOBALARGS.PARAM2=="INVALID":
        print('[PythonTemplate_Argparse: SIMULATE ERROR] Invalid Detected for PARAM1 and PARAM2.\n\n')
        parser.print_help()
        sys.exit(1)


def main():
    ProccessCmdLineArgs()
    print(GLOBALARGS)

if __name__ == '__main__':
	main()