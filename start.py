from datetime import datetime

def showtime()->None:
    print(datetime.now())

showtime()

def greet(name: str)->None:
    print(f"hello ,{name}!")

greet("sajan")