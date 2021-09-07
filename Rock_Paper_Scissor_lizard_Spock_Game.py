import random

# BBT Sheldon Inspired Rock Paper Scissor Lizard Spock Game

def GameWin(comp, you):
    # If two values are equal, declare a tie!
    if comp == you:
        return None

    # Check for all possibilities when computer chose r
    elif comp == 'r':
        if you=='p':
            return True
        elif you=='s':
            return False
        elif you=='l':
            return False
        elif you=='sp':
            return True
    
    # Check for all possibilities when computer chose p
    elif comp == 'p':
        if you=='r':
            return False
        elif you=='s':
            return True
        elif you=='l':
            return True
        elif you=='sp':
            return False
        
    
    # Check for all possibilities when computer chose s
    elif comp == 's':
        if you=='r':
            return True
        elif you=='p':
            return False
        elif you=='l':
            return False
        elif you=='sp':
            return True

    # Check for all possibilities when computer chose l
    elif comp == 'l':
        if you=='r':
            return True
        elif you=='p':
            return False
        elif you=='s':
            return True
        elif you=='sp':
            return False

    # Check for all possibilities when computer chose sp
    elif comp == 'sp':
        if you=='r':
            return False
        elif you=='p':
            return True
        elif you=='s':
            return False
        elif you=='l':
            return True


print("Computer's Turn: Rock(r) Paper(p) Scissor(s) Lizard(l) Spock(sp)? ")
randNo = random.randint(1, 5) 
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'
elif randNo == 4:
    comp = 'l'
elif randNo == 5:
    comp = 'sp'    

you = input("Your Turn: Rock(r) Paper(p) Scissor(s) Lizard(l) Spock(sp)? ")
a = GameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")