your_name = input("Welcome to the Love Calculator!\nYour name :\n").lower()
partner_name = input("Your partner's name:\n").lower()
t_count = your_name.count("t") + partner_name.count("t")
r_count = your_name.count("r") + partner_name.count("r")
u_count = your_name.count("u") + partner_name.count("u")
e_count = your_name.count("e") + partner_name.count("e")
l_count = your_name.count("l") + partner_name.count("l")
o_count = your_name.count("o") + partner_name.count("o")
v_count = your_name.count("v") + partner_name.count("v")
e_count = your_name.count("e") + partner_name.count("e")
true_count = t_count + r_count + u_count + e_count
love_count = l_count + o_count + v_count + e_count
true_love = str(true_count) + str(love_count)
true_love_score = int(true_love)
if 10 < true_love_score > 90:
    print(f"Your score is {true_love_score}, you go together like coke and mentos.")
elif 40 < true_love_score > 50:
    print(f"Your score is {true_love_score}, you are alright together")
else:
    print(f"Your score is {true_love_score}")