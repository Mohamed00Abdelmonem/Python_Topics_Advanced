
import typer



def sum(x:int, y:int): # type hint
    print(x+y)

def mul(x:int, y:int):
    print(x*y)
 

if __name__=='__main__':
    app = typer.Typer()
    app.command()(sum)
    app.command()(mul)
    app()
    