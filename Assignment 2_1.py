import random
x = random.randint (0, 20)
count = 0
for i in range(5):
    user_number = int(input("Enter your number: "))
    count = count + 1
    if x == user_number:
        print("congrts", " you tried", count, "times")
        break
    elif x > user_number:
        print("up")
    elif x < user_number:
        print("down")
        