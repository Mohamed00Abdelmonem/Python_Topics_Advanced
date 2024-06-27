import typer

app = typer.Typer()

@app.command()
def calc(salary:int, employee:bool=False):
    if employee:
        tax = salary * 0.85
        print(tax)
        return
    
    print( salary * 0.90)


if __name__== "__main__":
    app()