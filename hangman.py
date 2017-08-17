import random

def getrandomword():
    lines = open('words.txt').read().splitlines()
    myline =random.choice(lines)
    return myline

def printch(a):
    for i in range(len(a)):
        print("",a[i],end="")

if __name__ == '__main__':
    new = 'Y'
    while(new=='Y'):
        word = getrandomword().upper()
        cover = []; incorrect = []
        for _ in range(len(word)):
            print(" _",end="")
            cover.append("_")
        print("")
        limbs = 5
        while(limbs>0):
            guess = input("Enter a letter to guess: ").upper()
            count = 0
            for i in range(len(word)):
                if(guess==word[i]):
                    count = count + 1
                    cover[i]=guess
            if((count==0) and (guess not in incorrect)):
                incorrect.append(guess)
                print("Sorry",guess,"is not in the word")
                limbs = limbs - 1
            print("Limbs left: ",limbs)
            printch(cover)
            print("\nIncorrect guesses:",end="")
            printch(incorrect); print("\n")
            if("_" not in cover):
                print("\nYou win!")
                new = input("New game [Y/N] ? ")
                print("\n")
                break
        if(limbs==0):
            print("\nYou lose!")
            print("The word was:",end="")
            printch(word)
            print("\n")
            new = input("New game [Y/N] ? ").upper()
            print("\n")
