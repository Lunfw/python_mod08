from os import path, environ, name
from sys import executable, prefix, stderr
from site import getsitepackages


class GeneralErrors(Exception):
    pass


class EnvErrors(GeneralErrors):
    pass


def in_env_output():
    print("\nSUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.\n")
    print('Package installation path:')
    print(f"{getsitepackages()[0]}")


def out_env_output():
    '''
        #   Output message for when the script is not running inside a venv.
    '''
    print("\nWARNING: You're not in the global environment!")
    print('The machines can see everything you install.\n')

    print('To enter the construct, run:')
    print('python -m venv matrix_env')
    if (name == 'posix'):
        print('source matrix_env/bin/activate')
    print('matrix_env')
    print('Scripts')
    if (name == 'nt'):
        print('activate')
    print('\nThen run this program again.')


def main_exec():
    '''
        #   Whether the script is running inside a venv or not.
    '''
    venv: bool = ('VIRTUAL_ENV' in environ)
    try:
        if (venv):
            print('Welcome to the construct\n')
        else:
            raise EnvErrors("You're still plugged in\n")
    except EnvErrors as ee:
        print(f"{ee}", file=stderr)

    try:
        print(f"Current Python: {executable}")
        if (not venv):
            raise EnvErrors("None detected")
        print(f"Virtual Environment: {path.basename(prefix)}")
        print(f"Environment Path: {prefix}")
    except EnvErrors as ee:
        print(f"Virtual Environment: {ee}", file=stderr)

    if (venv):
        in_env_output()
    else:
        out_env_output()


def main():
    '''
        #   Small main program.
    '''
    print('\nMATRIX STATUS: ', end='')
    main_exec()


if (__name__ == '__main__'):
    main()
