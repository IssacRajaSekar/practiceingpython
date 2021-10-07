print("Welcome to the Tip calculator!")
total_bill = float(input("What was the total bill?\n"))
number_of_people = int(input("How many people to split the bill?\n"))
tip_percentage = int(input("What percentage tip would you like to give?\n"))
tip_amount = total_bill / tip_percentage
each_person_bill = '{0:.2f}'.format((total_bill + tip_amount) / number_of_people)
print(f"Each person should pay Rs: {each_person_bill}")

