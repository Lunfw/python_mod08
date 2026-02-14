from os import path
from sys import exit
from numpy import array


def get_pandas() -> bool:
    '''
        #   Check if pandas is installed and print its version.
    '''
    import pandas as p
    if (p.__version__):
        print(f'[OK] pandas ({p.__version__}) - Data manipulation ready')
        return (True)
    print('[KO] package pandas does not exist')
    return (False)


def get_requests() -> bool:
    '''
        #   Check if requests is installed and print its version.
    '''
    import requests as r
    if (r.__version__):
        print(f'[OK] requests ({r.__version__}) - Network access ready')
        return (True)
    print('[KO] package requests does not exist')
    return (False)


def get_matplotlib() -> bool:
    '''
        #   Check if matplotlib is installed and print its version.
    '''
    import matplotlib as plt
    if (plt.__version__):
        print(f'[OK] matplotlib ({plt.__version__}) - Visualization ready')
        return (True)
    print('[KO] package matplotlib does not exist')
    return (False)


def main_exec() -> bool:
    '''
        #   Main execution program.
    '''
    print('Checking dependencies:')
    try:
        import matplotlib.pyplot as plt
        get_pandas()
        get_requests()
        get_matplotlib()
    except Exception as e:
        print(f'Error checking dependencies: {e}')
        return

    print('\nAnalyzing Matrix data...')
    print('Processing 1000 data points...')
    print('Generating visualisation...\n')

    try:
        from pandas import Series
        n = array([1, 2, 3, 4, 5])
        s = Series(n, index=[1, 2, 3, 4, 5])
        s.plot(kind='bar')
        plt.ylabel('wtf am i doing')
        plt.xlabel('SIX. SEVEN.')
        plt.title('aura monster graph')
        plt.savefig('matrix_analysis.png')
    except Exception as e:
        print(f'Error loading dependencies: {e}')
        return (False)
    return (True)

def main() -> None:
    '''
        #   Small main program.
    '''
    print('\nLOADINGS STATUS: Loading programs...\n')
    if (main_exec()):
        print('Analysis complete!')
        print('Results saved to: matrix_analysis.png')
        exit(1)
    print('Analysis could not be completed.')

if (__name__ == '__main__'):
    main()
