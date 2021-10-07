rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
game=[rock, paper, scissors]
your_choice=int(input("Make your choice, 0 for rock, 1 for paper, 2 for scissors."))
if your_choice>=3 or your_choice<0:
  print("invalid number")
else:
  print(game[your_choice])
  print("computer choose")
  c_choice=random.randint(0,2)
  print(game[c_choice])
  if your_choice==c_choice:
    print("draw")
  if your_choice==rock and c_choice==scissors:
    print("you win")
  if your_choice==scissors and c_choice==rock:
    print("you lose")
  if your_choice<c_choice:
    print("you lose")
  if your_choice>c_choice:
    print("you win")
