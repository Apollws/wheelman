# A 'Hangman' game that is 'wheel-of-fortune' style.

import random
import time
import datetime

with open("lexicon.txt", "r") as lexeis:
    lexicon = lexeis.read().split('\n')
    lexicon = [tuple(element.split(',')) for element in lexicon]
  
class Player:
    def __init__(self, name: str, money: int):
        self.name = name
        self.money = money

    def update(self, amount: int):
        self.money += amount

class Traced_Word:
    def __init__(self, word: tuple):
        self.word = word[0]
        self.definition = word[1]
        # PoS (Part of Speech)
        self.PoS = word[2]

        self.word_as_list = list(self.word)
        self.length = len(self.word)
        self.traced_word = list(enumerate(self.word))
        self.filled_word = ['-' for i in range(self.length)]
        
    def is_success(self) -> bool:
        if '-' not in self.filled_word:
            print(f'The word is "{"".join(self.filled_word)}".')
            return True
        else:
            return False
    
    def guess_word(self, player: Player):
        unfold(f"{player.name}, type the word, and press 'Enter'. ")
        my_word = input().lower()
        if my_word == self.word:
            earning = self.filled_word.count("-") * 200
            unfold(f"Bravo, {player.name}! You earned {earning} points!\n")
            wait(5)
            player.update(earning)
            unfold(f"You now have {player.money} in your account.\n")
            self.filled_word = my_word
        else:
            unfold("Wrong guess! Try again some other time.\n")
            wait(5)
            player.update(-200)
            unfold(f"You now have {player.money} in your account.\n")
        
    def guess_consonant(self, player: Player):
        while True:
            unfold(f"{player.name}, choose your consonant and press 'Enter'. ")
            consonant = input().lower()
            if len(consonant) > 1:
                print("Only one letter!")
            else:
                if consonant.lower() not in "bcdfghjklmnpqrstvwxz":
                    print("Not a consonant!")
                    break
                elif consonant.lower() not in self.word:
                    print(f"'{consonant}' not found!")
                    break
                else:
                    for (i, c) in self.traced_word:
                        if c == consonant.lower():
                            self.filled_word[i] = c
                            player.update(100)
                    print(f"You now have {player.money} in your bank account.")
                    break
    
    def buy_clue(self, player: Player):
        while True:
            unfold(f"{player.name}, type either [D]efinition or [P]art of Speech. ")
            clue_type = input().lower()
            if clue_type == 'd':
                player.update(-100)
                unfold(f"{self.definition}\nYou now have {player.money} left in your bank account.\n")
                break
            elif clue_type == 'p':
                player.update(-100)
                unfold(f"{self.PoS}\nYou now have {player.money} left in your bank account.\n")
                break
            else:
                print("You can only type 'D' or 'P'.")
                continue


    def buy_vowel(self, player: Player):
        while True:
            unfold(f"{player.name}, pick a vowel and press 'Enter'. ")
            vowel = input().lower()
            if len(vowel) > 1:
                print("Only one letter!")
            else:
                player.update(-100)
                if vowel not in self.word:
                    print("'{vowel}' not found!")
                    break
                else:
                    for (i, v) in self.traced_word:
                        if v == vowel:
                            self.filled_word[i] = v
                    break
                    
def wait(waiting_time):
    time.sleep(waiting_time/10)
    
 
def unfold(text: str):
    for letter in text:
        print(f"{letter}", end="")
        wait(0.1)
        
def intro():
    unfold("Welcome to the 'Wheelman', a hybrid of 'Hangman' and 'Wheel of Fortune'!")
    print()
    wait(3)
    unfold("Please, enter your name or nickname: ")

def greeting(player: Player):
    unfold(f"{player.name}, you have {player.money} in your bank account.")
    print()
    wait(3)
    unfold("Use them wisely.")
    print()
    wait(3)
    unfold("Good luck!")
    print()
    wait(3)

class Game:
    def __init__(self, player: Player, traced_word: Traced_Word):
        self.player = player
        self.two = traced_word

    def rec_score(self):
        with open("scores.txt", "a") as file:
            file.write(f"{datetime.datetime.now()}\t{self.player.name}\t{self.player.money}")

    def play(self):
        while not self.two.is_success():
            unfold("".join(self.two.filled_word))
            print()
            unfold(f"{self.player.name}, guess the [W]ord, guess a [C]onsonant, "
                   f"buy a [V]owel, buy a [H]int, or [Q]uit: ")
            option = input().lower()[0]

            if option == 'w':
                self.two.guess_word(self.player)
            elif option == 'c':
                self.two.guess_consonant(self.player)
            elif option == 'v':
                self.two.buy_vowel(self.player)
            elif option == 'h':
                self.two.buy_clue(self.player)
            elif option == 'q':
                break
            else:
                print("The only available options are 'W', 'C', 'V', 'H' and 'Q'.")
        self.rec_score()

        
#   Main:

intro()
name = input()
# Player (o b j e c t)
my_player = Player(name, 200)
wait(3)
greeting(my_player)
# Word To Guess (t u p l e)
word2guess = random.sample(lexicon, k=1)[0]
# Traced_Word (o b j e c t)
two = Traced_Word(word2guess)
game = Game(my_player, two)    
game.play()
