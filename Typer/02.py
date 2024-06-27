
# pip install Typer

import typer

app = typer.Typer()


@app.command()
def sum(x:int, y:int): # type hint
    print(x+y)

@app.command()
def mul(x:int, y:int):
    print(x*y)
 

if __name__=='__main__':
    app()
    