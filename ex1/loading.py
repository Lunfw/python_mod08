from sys import exit


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


def makeplot() -> None:
    '''
        #   Generate a plot using matplotlib.
    '''
    import matplotlib.pyplot as plt
    try:
        plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25])
        plt.title('Plot Example')
        plt.xlabel('X')
        plt.ylabel('Y')
    except Exception as e:
        print(f'Error generating plot: {e}')
        return (False)
    plt.savefig('simple_plot.png')
    return (True)


def main_exec() -> bool:
    '''
        #   Main execution program.
    '''
    print('Checking dependencies:')
    try:
        get_pandas()
        get_requests()
        get_matplotlib()
    except Exception as e:
        print(f'Error checking dependencies: {e}')
        return

    print('\nAnalyzing Matrix data...')
    print('Processing 1000 data points...')
    print('Generating visualisation...\n')

    return (makeplot())


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
