from time import sleep
from random import randint

Difficulties = ('easy', 'medium', 'hard', 'brutal')
# 0 values for wrapping during enumeration
LifeDifficulty = (10, 5, 3, 1, 0)
WordDifficulty = (3, 6, 10, 13, 0)

def wordLengthList(wordList: tuple):
	wordVals = {}
	for word in wordList:
		if len(word) in wordVals:
			wordVals[len(word)] += 1
		else:
			wordVals[len(word)] = 1

	print(sorted(wordVals.items()))

def userSetDifficulty():
	choice = -1
	diffLen = len(Difficulties)
	while 0 >= choice or choice > diffLen:
		for i, diff in enumerate(Difficulties):
			print(f"{i} - {diff}")
		rawInput = input()
		if bool(rawInput) and 0 <= int(rawInput) < diffLen:
			choice = int(rawInput)
		else:
			print('\nchoice out of bounds\n')
			sleep(1)

	return choice

def getWordFromList(wordList: list, diff: int):
	word = ''
	wordDiffMin = WordDifficulty[diff - 1]
	wordDiffMax = WordDifficulty[diff]

	while not bool(word) or wordDiffMin <= len(word) <= wordDiffMax:
		tempWord = wordList[randint(0, len(wordList) - 1)]
		if len(tempWord) > wordDiffMax:
			continue
		elif len(tempWord) > wordDiffMin and len(tempWord) <= wordDiffMax:
			word = tempWord
			break

	return word.lower()

def getLives(diff: int):
	return LifeDifficulty[diff]

