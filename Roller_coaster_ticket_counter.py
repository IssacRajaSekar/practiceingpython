height = int(input("Welcome to the RollerCoaster!\nWhat is your height?\n"))
if height > 120:
    bill = 0
    age = int(input("What is your age?\n"))
    if age < 12:
        bill = 5
    elif age < 18:
        bill = 7
    elif age >= 45 and age <= 55:
        print("Enjoy a Free Ride!\n")
    else:
        bill = 12
    wants_photo = input("Do you want a photo taken? type Y or N\n").lower()
    if wants_photo == "y":
        bill += 3
    print(f"Your bill is:{bill}")

else:
    print("Sorry,You have grow higher before riding the roller coaster:)")

