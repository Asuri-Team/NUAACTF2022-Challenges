from random import randint,shuffle
from random import choice
import os

flag = os.environ.get('FLAG')
white_list = ['==','(',')','C0','C1','C2','C3','C4','C5','C6','C7','C8','C9','C10','0','1','and','or','not']

def calc(ans, chests, expr):
	try:
		C0, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10 = chests
		r = eval(expr)
	except Exception as e:
		print("The god fails to understand your words.\n",e)
		exit(0)
	return ans(r)

def do_round():
	truth=lambda r: not not r
	lie=lambda r: not r
	chests=[]
	for i in range(11):
		chests.append(choice((True,False)))
	print("Eleven chests lie here, with mimics or real keys hidden inside.\nBut don't worry. The god will help you.")
	Patches=[truth]*14+[lie]*1
	shuffle(Patches)
	for i in range(15):
		print("Ask for the god:")
		question=input().strip()
		for word in question.split(" "):
			if word not in white_list:
				print("({}) No keys for dirty hacker!".format(word))
				exit(0)
		res=str(calc(Patches[i], chests, question))
		print('The god answers: {}!\n'.format(res))
	print("Now open the chests:")
	return chests == list(map(int, input().strip().split(" ")))

print("You are now arriving the dragon's home. But the keys of the door are disappear.")
print("There are only, however, eleven chests with the keys or mimics.")
print("Eleven gods will help you, with a evil god who is pretended by the dragon.")
print("Can you still get all the real keys without losing your mind?")

for i in range(100):
	if not do_round():
		print("The dragon comes here and BITE YOUR HEAD OFF.\n")
		exit(0)
	else:
		print("You take all the keys safe and sound. Head to the next vault!\n")

print(f"You've found all the keys!\n {flag}")


