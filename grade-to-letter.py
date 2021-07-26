import sys
import json
from types import SimpleNamespace
# Given a student's score on a test, return a letter grade

gradeNS = SimpleNamespace(
	aHigh= 100,
	aLow= 90,
	bHigh= 89,
	bLow= 80,
	cHigh= 79,
	cLow= 70,
	dHigh= 69,
	dLow= 60,
	fHigh= 59,
	fLow= 0
)

def convertPercentToGrade(val, gradeNS):
	if gradeNS.fLow <= val <= gradeNS.fHigh:
		return 'F'
	elif gradeNS.dLow <= val <= gradeNS.dHigh:
		return 'D'
	elif gradeNS.cLow <= val <= gradeNS.cHigh:
		return 'C'
	elif gradeNS.bLow <= val <= gradeNS.bHigh:
		return 'B'
	elif gradeNS.aLow <= val <= gradeNS.aHigh:
		return 'A'
	else:
		return 'ERROR - Out of bounds'

def gradeToLetter(val, total, gradeNS):
	if val > 100 and (not bool(total)):
		print(UserWarning('ERROR - Values over 100 need a "total" arg to divide by'))
	elif not total:
		print(f"Grade: {convertPercentToGrade(val, gradeNS)}")
	elif total:
		print(f"Grade: {convertPercentToGrade(val / total * 100, gradeNS)} - {val / total * 100}")
	else:
		print('invalid value')

def handleInput():
	'''
	Takes up to 3 arguments
		val: value as percentage correct
		total: changes functionality to # correct out of 'total'
		gradeNS: user provided JSON object to change the default scoring
			- keys must use double quotes
			- e.g. ... 10 10 '{"aHigh": 50, "aLow": 20, ... }'
	'''
	try:
		userBaseVal = int(sys.argv[1]) if len(sys.argv) > 1 else int(input("What's the grade / value? "))
	except Exception as e:
		print(e)
		return

	try:
		totalValInput = sys.argv[2] if len(sys.argv) > 2 else input("Opt: Total points? ")
		userTotalVal = int(totalValInput) if bool(totalValInput) else False
	except Exception as e:
		print(e)
		return

	userGradeNS = sys.argv[3] if len(sys.argv) > 3 else input("Opt: Custom grading?\n")
	if len(userGradeNS):
		try:
			parseGradeNS = json.loads(
				userGradeNS,
				object_hook=lambda d: SimpleNamespace(**d)
			)
		except json.decoder.JSONDecodeError as e:
			print("Does the provided object start with quotes? eg: '{...}' ")
			print(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}")
			return

	gradeToLetter(
		userBaseVal,
		userTotalVal,
		parseGradeNS if bool(userGradeNS) else gradeNS
	)

handleInput()

'''
python grade-to-letter.py 10 100 '{"aHigh": 100,"aLow": 90,"bHigh": 89,"bLow": 80,"cHigh": 79,"cLow": 70,"dHigh": 69,"dLow": 60,"fHigh": 59,"fLow": 0}'
'''