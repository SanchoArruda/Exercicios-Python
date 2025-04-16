def announce(f):
    def wrapper():
        print("Inicinado a funcao...")
        f()
        print("A funcao foi concluida")
    return wrapper    


@announce
def hello():
    print("Hello, world!")


hello()