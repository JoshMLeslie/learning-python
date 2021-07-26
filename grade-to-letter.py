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

'''
Takes up to 3 arguments
	val: value as percentage correct
	total: changes functionality to # correct out of 'total'
	gradeNS: user provided JSON object to change the default scoring
		- keys must use double quotes
		- e.g. '{"aHigh": 50, "aLow": 20, ... }'
'''
def handleInput():
	if len(sys.argv) > 1:
		parseGradeNS = {}
		if len(sys.argv) > 3:
			try:
				parseGradeNS = json.loads(
					sys.argv[3],
					object_hook=lambda d: SimpleNamespace(**d)
				)
				print(parseGradeNS)
			except Exception as e:
				print("Error processing provided grading NS")
				print(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}")
				return
				
		gradeToLetter(
			int(sys.argv[1]),
			int(sys.argv[2]) if len(sys.argv) > 2 else False,
			parseGradeNS if len(sys.argv) > 3 else gradeNS
		)
	else:
		userBaseVal = input("What's the grade / value? ")
		if not bool(userBaseVal):
			print('Must provide a grade / val')
			return
		
		userTotalVal = input("Opt: Total points ")
		userGradeNS = input("Opt: Custom grading NSionary")

		print(userGradeNS)
		if bool(userGradeNS):
			parseGradeNS = {}
			try:
				parseGradeNS = json.loads(
					userGradeNS,
					object_hook=lambda d: SimpleNamespace(**d)
				)
			except:
				print("Error processing provided grading NS")
				

		gradeToLetter(
			int(float(userBaseVal)),
			int(float(userTotalVal)) if bool(userTotalVal) else False,
			parseGradeNS if bool(parseGradeNS) else gradeNS
		)

handleInput()

'''
python grade-to-letter.py 10 100 '{"aHigh": 100,"aLow": 90,"bHigh": 89,"bLow": 80,"cHigh": 79,"cLow": 70,"dHigh": 69,"dLow": 60,"fHigh": 59,"fLow": 0}'
'''