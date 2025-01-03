from datetime import datetime
import calendar
def showtime()->None:
    print(datetime.now())
    print(calendar.calendar(int(2025)))
showtime()

def greet(name: str)->None:
    print(f"hello ,{name}!")

greet("sajan")

