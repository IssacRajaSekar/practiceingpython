import random

name_string = input("Give me everybody's names, seperated by a comma:\n")
name = name_string.split(",")
length_of_the_list = len(name)
random_num = random.randint(0, length_of_the_list-1)
bill_payer = name[random_num]
print("Today " + bill_payer + " is going to pay the bill")