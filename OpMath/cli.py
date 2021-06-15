from OpMath import *

import click

@click.command()
@click.option("-m", '--func', help='function', required=True)
@click.option("-n1", '--num1', help='num1', required=True)
@click.option("-n2", '--num2', help='num2', required=True)

def main(func, num1, num2):
    if func=="soma":
        num1 + num2
    elif func=="sub":
        num1 - num2
    else:
        print("Introduza 'soma', ou 'sub'.")

if __name__ == '__main__':
    main()