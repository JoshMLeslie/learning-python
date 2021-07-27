from hangman import startGame
from hangman_words import wordList
from hangman_util import Difficulties, wordLengthList, userSetDifficulty, getWordFromList, getLives

difficulty = 0

print('Welcome to Hangman!\nPlease select an option or press enter to start:')
choice = -1
while choice != 0:
	print(f'0 - Start')
	print(f'1 - Set difficulty ({Difficulties[difficulty]})')
	print(f'2 - See word-length list')
	rawInput = input()
	try:
		choice = int(rawInput) if bool(rawInput) else 0
	except Exception as e:
		print(e)
		choice = -1

	if choice == 0:
		startGame(
			getWordFromList(wordList, difficulty),
			getLives(difficulty)
		)
	elif choice == 1:
		difficulty = userSetDifficulty()
	elif choice == 2:
		wordLengthList(wordList)
