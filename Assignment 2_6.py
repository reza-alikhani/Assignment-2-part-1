import random
while True:
    y = input("Tas mirizi? ")
    if y == "yes" or "are":
        x = random.randint(1, 6)
        print(x)
        if x == 6:
            print("Bordi, dobare tas beriz")

        else :
            print ("bakhti")



