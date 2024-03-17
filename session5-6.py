name = input("What is your name?\n")
age = input("How old are you?\n")
try:
    age = int(age)
    print("Hello ", name, "!", sep="")
    birthYear = 2024 - age
    print("Your birth year is ", birthYear, sep="")
    number = input("give me a div number\n")
    number = int(number)
    print(age / number)
except ValueError:
    print("You crazyyy, put a bloody number")
except ZeroDivisionError:
    print("You crazyyy, dividing by zero???")
except:
    print("WOAH IM SURPRISED ")
else:
    print("all good")
finally:
    print("Goodbye")
