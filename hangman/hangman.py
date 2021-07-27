def findIndicies(word, letter):
	indicies = []
	for i, ch in enumerate(word):
		if ch == letter:
			indicies.append(i)
	return indicies

def startGame(word: str, lives: int):
	wordFiller = []
	correctLetters = 0

	for ch in word:
		if ch == ' ':
			correctLetters += 1
			wordFiller.append(' ')
		else:
			wordFiller.append('-')

	print(word)

	while correctLetters < len(word) and lives > 0:
		print(f'Your word: {" ".join(wordFiller)}')
		guess = input('Guess a letter!\n')
		if not bool(guess):
			continue

		if guess in wordFiller:
			print('\nRepeat value, guess again!\n')
		elif guess in word:
			idx = findIndicies(word, guess)
			correctLetters += len(idx)
			for i in idx:
				wordFiller[i] = guess
		else:
			lives -= 1

	print(f'\nThe word was {word}')
	if lives > 0:
		print('You solved it! Congratulations!')
	else:
		print('Better luck next time!')
