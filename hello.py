from datetime import date

def say_hello(name):
    print("Hello, " + name)

say_hello("VS Code")
def say_day_of_week(date):
    print("Today is " + date.strftime("%A"))

say_day_of_week(date.today())