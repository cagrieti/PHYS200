import random
import time #this is only for a nicer interface it has nothing to do with the "ACTUAL" project
print("Welcome to HANGMAN: Human vs. Computer. Here, you can play the classical hangman against your own computer.") 
while True:
    print("Press ENTER to start! or press CTRL + C to exit! If you don't know how to play, type H.")
    inp = input()
    if inp == "h" or inp == "H" or inp == "":
        break
    else:
        print("INVALID INPUT")

u=0
while u<1:
    if inp == "H" or inp == "h":
        print("""Pff. You've never played this game before? Where were you living? In a cave?
Anyways, here how it goes. I choose a random word off of my mind. And then you start guessing the letters.
You can have 6 wrong guesses at most. (every time you guess a letter wrong, I draw one part of the man. When the man is complete, he hangs and you lose.
If you want to, you can guess the word right away, but if you guess it wrong the man will also die RIGHT AWAY! Are you smart enough to save this virtual man's life?""") #########################################
        u = 1
        input("\nNow that you've learned how to play, press ENTER to start!")
    else:
        break
pics = ['''
        +----+
             |
             |
             |
            ===''', '''
        +----+
        O    |
             |
             |
            ===''', '''
        +----+
        O    |
        |    |
             |
            ===''', '''
         +----+
         O    |
        /|    |
              |
             ===''','''
         +----+
         O    |
        /|\   |
              |
             === ''', '''
         +----+
         O    |
        /|\   |
        /     |
             ===''', '''
         +----+
         O    |
        /|\   |
        / \   |
             ===''']
play = True
while play:
    while True:
        d = input("\nPlease choose the difficulty level:\nType E for Easy, M for Medium and H for Hard: ")
        d = d.upper()
        words = []
        easy = ["PHYSICS", "PYTHON", "CODING", "APPLE", "BANANA", "PEN", "COMPUTER", "BOOK"]
        medium = ["MATHEMATICS", "TELEVISION", "SKYSCRAPER", "RUG", "JAZZ"]
        hard = ["ABSURD", "GEOGRAPHY", "ANDROID", "CASABLANCA", "OWL", "MACARENA"]
        if d == "E":
            words = easy
            break
        elif d == "M":
            words = medium
            break
        elif d == "H":
            words = hard
            break
        else: print("WRONG INPUT! Please choose your difficulty by typing e, m or h.")
    print("\nLet me think of a nice word. Hmm...")
    time.sleep(2)
    print("Wait... I'm thinking.")
    time.sleep(2)
    print("Okay, I got it. Let's go!")
    time.sleep(0.5)
    
    r = random.randint(0,len(words)-1)
    word = words[r]
    letters = list(word)
    guesses = []
    wrong_guesses = []
    correct_guesses = []
    n=0
    
    empty = [" __ "] * len(word)
    e = ""
    for m in empty:
        e = e + m
    skip = True

    #### the first time the user guesses a letter is a little different so it is inside a separate while loop (i wanted to write a different sentence) 
    while True:
        guess = input(pics[0] + "             Wrong guesses:" + str(wrong_guesses) + "\n" + "\nWord: " + str(e) + "\n\nOkay...human...take your first guess. (If you want to GUESS THE WORD right away, type 0 and I will take you to the word guessing menu.): ")
        if guess.isdecimal() and guess != "0":
            print("\n\n\n\n\nYou can only guess LETTERS. If you want to guess a word type 0 (no other numerical values are allowed).")
            break
        else:
            guess = guess.upper()
            if len(list(guess)) != 1:
                print("\n\n\n\n\nPlease type only ONE letter. Or if you want to guess the word, type 0.")
                break
            else:
                if guess == "0":
                        word_guess = input("Okay. Guess the word. Be careful though. The virtual man may die because of you!")
                        word_guess = word_guess.upper()
                        if word_guess == word:
                            e = ""
                            for z in letters:
                                e = e + " " + z + " "
                            decision = input(pics[6] + "             Wrong guesses:" + str(wrong_guesses) + "\n\nWord: " + str(e) + "\n\nCONGRATULATIONS! YOU BEAT ME AND SAVED OUR VIRTUAL MAN! WANT TO PLAY AGAIN? (Y/N)") #### add the repeat block here.
                            decision = decision.upper()
                            skip = False
                            if decision == "N":
                                play = False
                            break
                        else:
                            e = ""
                            for z in letters:
                                e = e + " " + z + " "
                            decision = input(pics[6] + "             Wrong guesses:" + str(wrong_guesses) + "\n"+ "\nWord: " + str(e) + "\n\nHAHAHAHAHAHA. I WON, THE VIRTUAL MAN IS DEAD. DO YOU WANT TO PLAY AND LOSE AGAIN ? (Y/N)") ###repeat block here as well
                            decision = decision.upper()
                            skip = False
                            if decision == "N":
                                play = False
                            break
                else:
                    guesses.append(guess)
                    if guess in letters:
                        print("\n\n\n\n\nNICE! You've found a letter. Don't be so happy though, this doesn't mean you saved our virtual guy.")
                        correct_guesses.append(guess)
                        for a in range(len(letters)):
                            if letters[a] == guess:
                                empty[a] = letters[a]
                        e = ""
                        for i in empty:
                            e = e + " " + i + " "
                        break
                    else:
                        wrong_guesses.append(guess)
                        print("\n\n\n\n\nNope. This letter is not a part of the word!")
                        n = n + 1
                        break
# after the first guess, we have a single while loop that operates again and again which is similar to the first part of the game
    while skip:
                    guess = input(pics[n] + "             Wrong guesses:" + str(wrong_guesses) + "\n" + "\nWord: " + str(e) + "\n\nTake another guess. (If you want to GUESS THE WORD right away, type 0 and I will take you to the word guessing menu).: ")
                    if guess.isdecimal() and guess != "0":
                        print("\n\n\n\n\nYou can only guess LETTERS. If you want to guess a word type 0 (no other numerical values are allowed).")
                    else:
                        guess = guess.upper()
                        if len(list(guess)) != 1:
                            print("\n\n\n\n\nPlease type only ONE letter. Or if you want to guess the word, type 0.")
                        else:
                            if guess in guesses:
                                print("\n\n\n\n\nYou've already guessed that letter... Humans are not that smart...")
                            else:
                                if guess == "0":
                                    word_guess = input("Okay. Guess the word. Be careful though. The virtual man may die because of you!")
                                    word_guess = word_guess.upper()
                                    if word_guess == word:
                                        e = ""
                                        for z in letters:
                                            e = e + " " + z + " "
                                        decision = input(pics[n] + "             Wrong guesses:" + str(wrong_guesses) + "\n" + "\nWord: " + str(e) + "\n\nCONGRATULATIONS! YOU BEAT ME AND SAVED OUR VIRTUAL MAN! WANT TO PLAY AGAIN? (Y/N)") #### add the repeat block here.
                                        decision = decision.upper()
                                        if decision == "N":
                                            play = False
                                            break
                                        else:
                                            break
                                    else:
                                        e = ""
                                        for z in letters:
                                            e = e + " " + z + " "
                                        decision = input(pics[6] + "             Wrong guesses:" + str(wrong_guesses) + "\n" + "Word: " + str(e) + "\n\nHAHAHAHAHAHA. I WON, THE VIRTUAL MAN IS DEAD. DO YOU WANT TO PLAY AND LOSE AGAIN ? (Y/N)") ###repeat block here as well
                                        decision = decision.upper()
                                        if decision == "N":
                                            play = False
                                            break
                                        else:
                                            break
                                else:
                                    guesses.append(guess)
                                    if guess in letters:
                                        correct_guesses.append(guess)
                                        print("\n\n\n\n\nNice one. This is a part of the word but don't get too happy too soon!")
                                        for a in range(len(letters)):
                                            if letters[a] == guess:
                                                empty[a] = letters[a]  
                                    else:
                                        wrong_guesses.append(guess)
                                        print("\n\n\n\n\nNope. This letter is not a part of the word!")
                                        n = n + 1
                    e = ""
                    for i in empty:
                        e = e + " " + i + " "

                    if empty == letters:
                        decision = input(pics[n] + "             Wrong guesses:" + str(wrong_guesses) + "\n" + "\nWord: " + str(e) + "\n\nCONGRATULATIONS! You've saved the virtual man's life!!! I wouldn't expect a human to be this smart! Want to play again ? (Y/N)")
                        decision = decision.upper()
                        if decision == "N":
                            play = False
                            break
                        else:
                            break
                    elif n == 6:
                        e = ""
                        for z in letters:
                            e = e + " " + z + " "
                        decision = input(pics[n] + "             Wrong guesses:" + str(wrong_guesses) + "\n" + "\nWord: " + str(e) + "\n\nYou are too slow. The virtual guy of yours is dead. HAHAHAHAHAHA, I WON!\nDo you want to play again ? (Y/N)")
                        decision = decision.upper()
                        if decision == "N":
                            play = False
                            break
                        else:
                            break
print("Okay. See you later, human.")
input("press ENTER to exit")
