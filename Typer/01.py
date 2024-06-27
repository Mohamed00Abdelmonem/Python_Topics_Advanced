
# pip install Typer

import typer

def sum(x:int, y:int):
    print(x+y)


if __name__=='__main__':
    typer.run(sum)
    