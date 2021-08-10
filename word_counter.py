from functools import reduce

print("Please provide a filename")
fileName = input()

f = open(fileName, 'r')

acc = {}
for line in f:
	for word in line.split():
		try:
			acc[word] += 1
		except:
			acc[word] = 1

print(acc)

f.close()