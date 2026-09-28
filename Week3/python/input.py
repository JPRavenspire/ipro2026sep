name = input("What is your name? ")

print(f"Hello {name}!")

while True:

    age = input("What is your age?")

    try:
        number = int(age)
        if (number >= 120):
            raise Exception
        print(f"Your age is: {age}")
        break
    except:
        print("You didn't specify a valid age!")

