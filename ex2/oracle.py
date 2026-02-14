from os import path
from sys import stderr
from dotenv import load_dotenv
from typing import TextIO


def check_env() -> bool:
    '''
        #   Check whether .env exists or not in the current directory.
    '''
    if (not path.exists('.env')):
        print('# Could not load configuration!', file=stderr)
        print('# Make sure .env exists in the current directory.')
        print("\n-> 'cp .env.example .env' then run this program again.")
        return (False)
    return (True)


def read_env() -> None:
    '''
        #   Read environment variables from .env file.
    '''
    with open('.env', 'r') as file:
        for i in file:
            if ('=' in i):
                key, value = i.split('=')
                key = key.strip()
                value = value.strip()
                if (key and value):
                    print(f"{key}: {value}")


def lineno(file: TextIO, line: str) -> int:
    '''
        #   Retrieves the line number of the current line in a file.
    '''
    for i, l in enumerate(file):
        if (l.strip() == line):
            return (i + 1)
    return (0)


def find_secrets() -> None:
    '''
        #   Check whether .env contains hardcoded secrets.
    '''
    exclude: tuple = ('secret', 'password', 'token')
    with open('.env', 'r') as file:
        for lineno, line in enumerate(file, start=1):
            for word in exclude:
                if (word in line.lower()):
                    print('\033[31m', end='', file=stderr)
                    print(f'[KO] wtf, {word} in .env?! -> L{lineno}', file=stderr)
                    print('\033[0m', end='')
                    file.close()
                    return
        print('[OK] No hardcoded secrets detected')


def main_exec() -> None:
    '''
        #   Main execution program.
    '''
    env_exists: bool = check_env()
    if (not env_exists):
        exit(1)
    load_dotenv()
    print('Configuration loaded:')
    read_env()
    print('\nEnvironment security check:')
    find_secrets()
    if (not env_exists):
        print("[KO] .env file doesn't even exist")
    else:
        print('[OK] .env file properly configured')
    print('[OK] Production overrides available')


def main():
    '''
        #   Small main program.
    '''
    print('\nORACLE STATUS: Reading the Matrix...\n')
    main_exec()
    print('\nThe Oracle sees all configurations.')


if (__name__ == '__main__'):
    main()
