import random
from words import word_list

def get_word():
    word=random.choice(word_list)
    return word.upper()

def play(word):
    word_completion ="_" * len(word)
    guessed = False
    guessed_letters = []  #IT STORE THE GUESSED LETTERS
    guessed_words = []  #IT STORE THE GUESSED WORDS
    tries = 6

    print("LET'S PLAY HANGMAN! ")
    print(display_hangman(tries))
    print(word_completion)
    print("there are ",len(word)," letters in the word")
    print("\n")
    while not guessed and tries > 0:
        guess = input("please guess the letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("you already guessed the letter",guess)
            elif guess not in word:
                print(guess," is not in the word.")
                tries-=1
                print("tries left ", tries)
                guessed_letters.append(guess)
                print(display_hangman(tries))
                print(word_completion)
                print("\n")
            else:
                print("well done! ",guess," is in the word.")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess] #DOUBT #LIST COMPREHENSION
                #enumerate(iterable, start=0)
                ''' I HAVE SOME DOUBT HERE'''
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)  #string_name.join(iterables)
                print(word_completion)
                if "_" not in word_completion:
                    guessed = True

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("you already guessed the word",guess)
            elif guess != word:
                print(guess, " is not in the word.")
                tries-=1
                print("tries left ", tries)
                guessed_words.append(guess)
                print(display_hangman(tries))
                print(word_completion)
                print("\n")
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
            print(display_hangman(tries))
            print(word_completion)
            print("\n")

    if guessed:
        print("Congrats, You guessed the word! You win!")
    else:
        print("sorry, you ran out of tries, the word is " +word+ ", Maybe next time!")

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    while input("play again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)

if __name__ =="__main__":
    main()
