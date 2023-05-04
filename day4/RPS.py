import random

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

#Write your code below this line 👇

choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.'))


range = [rock,paper,scissors]

computer = random.randint(0,2)

print(range[choice])
print("computer chose:")
print(range[computer])

if((choice == 0 and computer == 2) or (choice == 1 and computer == 0) or (choice == 2 and computer == 1)):
    print('you win')
elif (choice == computer):
    print('draw')
else:
    print('you loose')