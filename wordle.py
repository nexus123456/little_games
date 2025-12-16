import random
import sys


def get_guess():
    while True:
        guess = input("\nwhat is you guess: ").upper() 
        if isinstance(guess, int) or isinstance(guess, float):
            print("you can not use numbers in you answer \n try again ")
        elif len(guess) == 5:
            return guess
        else:
            print(" your answer must be fiver letters long ")
            


#gets a word for the game
def get_words():
    
    # chacks to see if you give it a wordlist as a CSV if not the except gives a word from its short list
     try:
        file_name = sys.argv[1]
        get_file_word(file_name)

     except:
        wordlist = ["AAHED", "AALII", "AARGH", "AARTI", "ABACA", "ABACI", "ABACK", "ABACS", "ABAFT", "ABAKA" ,"ABAMP" ,"ABAND", "ABASE"]
        word = random.choice(wordlist)
        return(word)


def get_file_word(file_name):
    lists = []
    try:
        with open(file_name) as file:
            for word in file: 
                word = word.replace(" \n", "")
                lists.append(word)
        random_word = random.choice(lists)
        return random_word
    except:
        print("can't find that word list ): ")

def check_words():
    word = get_words()
    i = 1
    guesses = ""

    while i <= 5:
        print("")
        guess = get_guess()
        count = 0
        for letter in guess:
            if letter == word[count]:
                guesses += "O"
            elif letter in word:
                guesses += "!"
            else:
                guesses += "X"
            count += 1
            
        print(guesses)
        guesses += "\n"


        if guess == word:
                print("\n you win! good job")
                i = 5
        i += 1

print("'O' is the right letter in the right place")    
print("'!' is the right letter in the wrong place")    
print("'X' is the wrong letter in the wrong place", end="" )    

check_words()


