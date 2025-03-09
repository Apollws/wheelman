The project is a simple game, a kind of "Hangman", with some ideas from the "Wheel of Fortune".
You choose between picking a consonant, buying a vowel or a hint if you have enough money, or guessing the word.
The hints are: definition and/or part of speech.

I used OOP to make it easier to construct. Otherwise it would have been very complicated for me.
So, the classes are:
1) A Player class, which stores the name and the points of the player. There is an update method updating the "bank account" by adding or subtracting points.
2) The main class is Traced_Word, containing all the necessary data and methods for tracing the word.
To initialize the traced_word object, we take a tuple from the "lexicon.txt" containing the word, its definition, and what part of speech it is.
The options lead you to the proper methods, guess_word(), guess_consonant(), buy_clue(), buy_vowel().
The methods of the word to be found (Traced_Word) also use the update() method from the Player class because the actions of the player can create earnings or losses.
3) There is also a Game class, for combining the above objects and helping their cooperation. The play() method is a while loop that runs for as long as the word contains gaps ("-"). For that, it uses the is_success() method of the Traced_Word class.

I made a (global?) function unfold() which unfolds the letters of the printed messages, to make the app have a slightly more interesting feel.

I used the random, time, and datetime libraries which belong to the core Python libraries, so I guess they are not external.
