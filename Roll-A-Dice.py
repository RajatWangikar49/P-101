import random

response = str(input("Press y to roll : "))

while response == "y" :
    print("[-----]")
    print("[-", random.randint(1, 6), "-]")
    print("[-----]")

    response = str(input("Press y to roll and press n to end : "))