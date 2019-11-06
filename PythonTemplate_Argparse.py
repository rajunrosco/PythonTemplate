import argparse
import sys

ARG=None

def ProccessCmdLineArgs():
    global ARG
    parser = argparse.ArgumentParser(description='PythonTemplate_Argparse')
    parser.add_argument(    'PARAM1',
                            help='Required Parameter 1'
                        )
    parser.add_argument(    'PARAM2',
                            help='Required Parameter 2'
                        )                    
    parser.add_argument(    '--OPTION1',
                            action='store_true',
                            help='OPTION1 boolean'
                        )
    ARG = parser.parse_args()


    if ARG.PARAM1=="INVALID" and ARG.PARAM2=="INVALID":
        print('[PythonTemplate_Argparse: SIMULATE ERROR] Invalid Detected for PARAM1 and PARAM2.\n\n')
        parser.print_help()
        sys.exit(1)


def main():
    global ARG
    ProccessCmdLineArgs()
    print(ARG.PARAM1,ARG.PARAM2)

if __name__ == '__main__':
	main()