import string
import os
import sys
from random import choice

# This is my little hangman game written in python. It is based on
# implementations found in tutorials, but extended with additional functions
# implemented by myself to get more fluent with the language. I also added
# comments and documentation to make it more readable and understandable.
#
# @author Adrian Strzelczyk (287072)
class Python_Hangman_Game():
    MAX_GUESSES = 6
    HANGMAN_GUI = [
        """
            -----
            |   |
                |
                |
                |
                |
            ---------
        """,
        """
            -----
            |   |
            O   |
                |
                |
                |
            ---------
        """,
        """
            -----
            |   |
            O   |
            |   |
                |
                |
            ---------
        """,
        """
            -----
            |   |
            O   |
            |\  |
                |
                |
            ---------
        """,
        """
            -----
            |   |
            O   |
           /|\  |
                |
                |
            ---------
        """,
        """
            -----
            |   |
            O   |
           /|\  |
             \  |
                |
            ---------
        """,
        """
            -----
            |   |
            O   |
           /|\  |
           / \  |
                |
            ---------
        """]

    # This is the initialisation of the game. It resets all values and picks a
    # random word.
    def __init__(self):
        self.word = self.pick_random_word()
        self.incorrect = []
        self.correct = []
        self.progress = self.get_guessed_progress()
        self.gameover = False

    # Help function to get a random string out of the words file. File
    # needs to be in same folder.
    def pick_random_word(self):
        game_words = open('words.txt', 'r').readlines()
        words = [word.strip() for word in game_words]
        return choice(words)

    # Helper method to check if the guessed letter was already used within the
    # game. It should be found in correct or incorrect variable.
    def check_already_guessed(self, guess):
        return guess in self.correct + self.incorrect

    # Method to process the guess and assign to correct or incorrect variable.
    def process_guessed_letter(self, guess):
        if guess in self.word:
            self.correct.append(guess)
        else:
            self.incorrect.append(guess)

    # Method to return the progress string. If a letter is guessed it's shown,
    # if not it's replaced with a underscore. CHeck letter for letter in correct.
    def get_guessed_progress(self):
        return "".join(#
            [let# declaration
                if let in self.correct# show letter when it's in correct guesses
                else "_"# show underscore if not
                for let in self.word# for every letter in chosen word
            ])

    # Method to check if game is won or lost.
    def game_lost_or_won(self):
        global won_rounds
        global lost_rounds
        if len(self.incorrect) >= Python_Hangman_Game.MAX_GUESSES:
            self.gameover = True
            lost_rounds += 1
            return "\nYou lose. The word was %r." % self.word
        if set(self.correct) == set(self.word):
            self.gameover = True
            won_rounds += 1
            return "\nYou won!"
        return ""

    # Method to show the current progress aka game screen. __str__ is the
    # equivalent to toString() in java.
    def __str__(self):
        global rounds
        global won_rounds
        global lost_rounds
        os.system('clear')
        result = "This is your %s game. \n" % rounds
        result += "You have won %s rounds and lost %s rounds." % (won_rounds, lost_rounds)
        result += "\n" * 3
        result += Python_Hangman_Game.HANGMAN_GUI[len(self.incorrect)]
        result += "\nIncorrect guesses: %s" % ", ".join(self.incorrect)
        result += "\nProgress: %s" % self.get_guessed_progress()
        result += self.game_lost_or_won()
        return result

#--End of class-----------------------------------------------------------------

# Method to let the player guess a letter and checks the input if it's valid.
def guess_a_letter(game):
    while True:
        guess = raw_input("Guess a letter: ").lower()
        # check if length of input is lower than 1 and if it's lowercase
        # (in this case a letter and not a number or something else)
        if len(guess) > 1 or guess not in string.lowercase:
            print "\nPlease guess a letter."
        elif game.check_already_guessed(guess):
            print "\nYou've already guessed %r." % guess
        else:
           return guess

# Python system method and overall start of application.
if __name__ == "__main__":
    # on start of script.
    os.system('clear')
    print("***********************************************************")
    print("*** Hello this is my first python console application.  ***")
    print("*** Made by Adrian Strzelczyk (287072).                 ***")
    print("***********************************************************")
    # couldn't use the multiple lines string here cause of some weird behaviour.
    # Two lines were in one.
    print(" _ ")
    print("| | ")
    print("| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __")
    print("| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ ")
    print("| | | | (_| | | | | (_| | | | | | | (_| | | | | ")
    print("|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|")
    print("                    __/ |")
    print("                   |___/")

    answer = raw_input("\nWant to start? (y/n): ").lower()
    if "y" in answer:
        keepGoing = True
    else:
        keepGoing = False
        print "Maybe next time!"
        sys.exit()
    # Start of game
    rounds = 1;
    won_rounds = 0;
    lost_rounds = 0;
    # Ingame routine.
    while keepGoing:
        game = Python_Hangman_Game()
        print game
        while not game.gameover:
            guess = guess_a_letter(game)
            game.process_guessed_letter(guess)
            print game
        # if gameover aks for another round.
        play_again = raw_input("Play again? (y/n): ").lower()
        if "n" in play_again:
            keepGoing = False
        else:
            rounds += 1
    # if user exits game.
    if rounds == 1:
        print "Thank you for playing one round of hangman!"
    else:
        print "Thank you for playing %s rounds of hangman!" % rounds
