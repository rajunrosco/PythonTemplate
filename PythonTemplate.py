# Python 3.6 Template
import getopt
import os
import sys
import shutil


# Reference to module located outside current project path relative to current script path
this_modulepath = os.path.dirname(os.path.realpath(__file__))
ExternalPath = this_modulepath+"\\..\\..\\..\\..\\Scripts\\ExternalModuleDirectory"

if os.path.exists(ExternalPath):
    sys.path.insert(0, ExternalPath)
    import externalmodule
#else:
#    sys.exit(-1)  # option to end script execution of external module is not found



def print_usage():
    """
    Help printout for current Script
    """

    print("")
    print("ScriptName <OPTIONS>")
    print("")
    print("  {: <15} {: >10}".format(*['-h, -?, --help','Displays this help output']))
    print("  {: <15} {: >10}".format(*['--test','Test Scriptname'])) 



######################################################################################################################################################################
#
# Main()
#
######################################################################################################################################################################
    

def Main(argv):



    try:
        opts, args = getopt.getopt(sys.argv[1:],
                                   '?h',                # each character represents a sort option -?, -H
                                   ['help','test1','test2=']      # each list entry represents a long option --help, etc.
                                   )
    except getopt.GetoptError as err:
        print (str(err))
        print_usage()
        sys.exit(2)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        print_usage()
        sys.exit(2)

    # Example:  python.exe PythonTemplate.py --test1 --test2=test2val file1 file2
    # Result:
    #    opts: [('--test1', ''), ('--test2', 'test2val')]
    #    args: ['file1', 'file2']
    print("opts: "+repr(opts))
    print("args: "+repr(args))

    for opt, val in opts:
        if opt in ['-?','-h','--help']:
            print_usage()
            sys.exit(0)
        if opt in ['--test1','--test2']:
            print('TEST MODE')




# If module is executed by name using python.exe, enter script through Main() method.  If it is imported as a module, Main() is never executed at it is used as a library
if __name__ == "__main__":
    Main(sys.argv)