import random
user_choice=int (input("enter choice: type 0 for rock, 1 for paper,2 for scissors."))
computer_choice = random.randint(0,2)
print("computer_choice")
print(computer_choice)
if user_choice== computer_choice:
    print("draw")
elif user_choice < computer_choice :
    print("loose")
elif computer_choice < user_choice :
    print ("win")
elif computer_choice == 0 and user_choice == 2:
    print ("loose")
elif computer_choice == 1 and user_choice == 2:
    print ("win")