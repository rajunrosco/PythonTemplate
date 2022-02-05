# Personal Python 3.7+ Template
import argparse
import getopt
import os
import pathlib
import sys

# global vars
G_ARGS = None

# current path of this module
G_modulepath = pathlib.Path.cwd()

# load modules external to this location
try:
    sys.path.insert(0, str( pathlib.Path.resolve(G_modulepath/'..'/'PythonExperiments'/'DateTimeTest') ))
    import DateTimeTest  # module from external PythonExperiments GitHub repository
    sys.path.insert(0, str( pathlib.Path.resolve(G_modulepath/'..'/'PythonExperiments'/'PandasTest') ))
    import PandasTEST  # module from external PythonExperiments GitHub repository
except ModuleNotFoundError as e:
    print("[EXCEPTION] {}".format(e.msg))
    sys.exit(1)

# custom exception for this module
class PythonTemplateException(Exception):
    def __init__(self, message="PythonTemplateException."):
        self.message = "[EXCEPTION] {}".format(message)
    def __str__(self):
        return f'{self.message}'

# retrieves environment variable or None if it does not exist
ENV_VAR = os.getenv("ENV_VARNAME")

def LOG(message):
    print("[Log] {}".format(str(message)))

def ERROR(message):
    print("[ERROR] {}".format(str(message)))

def ProccessCmdLineArgs():
    parser = argparse.ArgumentParser(description='PythonTemplate')
    #required positional string argument
    parser.add_argument(    'PARAM',
                            type=int,
                            help='Parameter'
                        )
    global G_ARGS  #required to modify global variable G_ARGS (not required to read it)
    G_ARGS = parser.parse_args()


def MethodWithException():
    raise PythonTemplateException("Something bad in MethodWithException")


######################################################################################################################################################################
#
# Main()
#
######################################################################################################################################################################
def Main(argv):
    ProccessCmdLineArgs()

    if G_ARGS.PARAM == 1:
        LOG("Hello")
    elif G_ARGS.PARAM ==2:
        LOG("Goodbye")
    else:
        try:
            MethodWithException()
        except PythonTemplateException as e:
            print(e.message)
        finally:
            sys.exit(1)

# If module is executed by name using python.exe, enter script through Main() method.  If it is imported as a module, Main() is never executed at it is used as a library
if __name__ == "__main__":
    Main(sys.argv)
        



