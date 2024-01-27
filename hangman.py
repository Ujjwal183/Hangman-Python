import random
print("Welcome TO Hangman")
print("--------------------------------------------------------")

wordDictionary = ["sunflower","Diamond","House","Memes","yeet"]

## choose a random word 

randomWord = random.choice(wordDictionary)

for x in randomWord :
    print("_",end="")

def print_hangman(wrong):
    if(wrong==0):
        print("\n+---+")
        print("    |")
        print("    |")
        print("    |")
        print("   ===")
    elif(wrong==1):
        print("\n+---+")
        print("O   |")
        print("    |")
        print("    |")
        print("   ===")
    elif(wrong==2):
        print("\n+---+")
        print("O   |")
        print("|   |")
        print("    |")
        print("   ===")
    elif(wrong==3):
        print("\n+---+")
        print(" O  |")
        print("/|  |")
        print("    |")
        print("   ===")
    elif(wrong==4):
        print("\n+---+")
        print(" O  |")
        print("/|\ |")
        print("    |")
        print("   ===")
    elif(wrong==5):
        print("\n+---+")
        print(" O  |")
        print("/|\ |")
        print("/   |")
        print("   ===")
    elif(wrong==6):
        print("\n+---+")
        print(" O  |")
        print("/|\ |")
        print("/ \ |")
        print("   ===")
        
def printword(guessedLetter):
    counter = 0
    rightLetter=0
    for char in randomWord:
        if(char in guessedLetter):
            print(randomWord[counter],end=" ")
            rightLetter+=1
        else:
            print(" ",end ="")
        counter+=1
    return rightLetter

def printLines():
    print("\r")
    for char in randomWord:
        print("\u203E",end=" ")

length_of_word_to_guess = len(randomWord)
amount_of_time_wrong = 0
current_guess_index = 0
current_letter_guess =[]
current_letter_right=0

while(amount_of_time_wrong!=6 and current_letter_right!=length_of_word_to_guess):
    print("\nLetter guessed so far :")
    for letter in current_letter_guess:
        print(letter,end=" ")
    letterGuessed = input("\nGuess a Letter : ")
        
    if(randomWord[current_guess_index]==letterGuessed):
        print_hangman(amount_of_time_wrong)
        current_guess_index+=1
        current_letter_guess.append(letterGuessed)
        current_letter_right = printword(current_letter_guess)
        printLines()
    else:
        amount_of_time_wrong+=1
        current_letter_guess.append(letterGuessed)
        print_hangman(amount_of_time_wrong)
        current_letter_right = printword(current_letter_guess)


print("Game is over ! Thank You for playing :)")    