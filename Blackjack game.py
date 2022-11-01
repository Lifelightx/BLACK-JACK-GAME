
import random

user_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
computer_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

u1 = random.choice(user_cards)
u2 = random.choice(user_cards)
print("The 1st card you choosed :",u1)
print("The 2st card you choosed :",u2)
u = u1 +u2
print("Total point : ",u)
c1 = random.choice(computer_cards)
c2 = random.choice(computer_cards)
print("1st card of computer :",c1)
print("2nd card of computer : ",c2)
c = c1 + c2
print("Total point of computer: ",c)
while u<21:
    ask = input("Do you want to pick up a card: ")
    if ask == 'yes':
        u3 = random.choice(user_cards)
        u = u3+ u
        print("you pick",u3)
        print("Total point of user = ",u)
    
    elif ask == 'no':
        break
while c<21:
    c3 = random.choice(computer_cards)
    c = c3+c
    print("computer pick",c3)
    print("Total point of computer: ",c)
if u>21:
    print("Computer own the game.")
elif c>21:
    print("You own the game.")
elif u>c:
    print("You own the game.")
elif c>u:
    print("Computer own the game.")
elif c==u:
    print("The match is draw.😂")


