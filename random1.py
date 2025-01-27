import random

lucky_num = int(input("Enter your lucky number (between 1 to 10): "))

while True:
    random_num = random.randint(1, 10)
    print(f"Generated random number: {random_num}")
    if random_num == lucky_num:
        print("Match found! Exiting the loop.")
        break
