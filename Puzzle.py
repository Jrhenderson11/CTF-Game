import os
import re
import random

def is_answer(test, answers):
	punc = [".",",","/","<",">",";",":","#","?","'","!", " "]
	t = test.lower()
	for symbol in punc:
		t.replace(symbol, "")
	for ans in answers:
		a = ans
		for symbol in punc:
			a.replace(symbol, "")
			a = a.lower()
		if t == a:
			return True
	return False

class Question(object):
	def __init__(self, ques, hints, ans, points=10):
		self.question = ques
		self.hints = hints
		self.answers = ans
		self.points = points

	def is_answer(self, text):
		if (is_answer(text, self.answers)):
			print "Correct!"
		else:
			print "Wrong"

class Score:
	def __init__(self, name):
		self.name = name
		self.score = 0
		self.questions_answered = []

	def ans_question(self, i, ans):
		if (test_ans(i, ans)):
			points = questions[i].points
			self.score = self.score + points
			print "Well done! you got " + points + " points"
		else:
			print "Sorry, that's not correct"

scores = []
questions = []

def test_ans(i, ans):
	questions[i].is_answer(ans)

def test_ans_interactive():
	print "enter question number:"
	num = int(raw_input())
	while (num<0 or num > len(questions)-1):
		os.system("/usr/bin/clear")
		print_menu()
		print "\033[31m	 invalid input \033[0m"
		print "enter question number to query:"
		num = int(raw_input())
	print "Question:"
	print questions[num].question
	print "Enter answer:"
	ans = raw_input()
	test_ans(num, ans)

def query_question():
	print "enter question number to query:"
	
	num = int(raw_input())
	while (num<0 or num > len(questions)-1):
		os.system("/usr/bin/clear")
		print_menu()
		print "\033[31m	 invalid input \033[0m"
		print "enter question number to query:"
		num = int(raw_input())

	print "Q:"
	print questions[num].question
	print "\nH:"
	print questions[num].hints
	print "\nA:"
	print questions[num].answers
	return

def get_q_from_file(fname):
	try:
		file = open(fname, 'r')
		#lines = file.readlines()
		text = file.read()
		file.close()
	except Exception as e:
		print "error opening " + fname

	i=1
	j=1
	k=1
	ques = []
	try:
		quesblocks = text.split("Q:\n")
		for block in quesblocks:
			#print block
			q, h, a = '','',''
			if not block == '':
				q = block.split("H:\n")[0].strip()
				print q
				h = (block.split("H:\n")[1]).split("A:\n")[0].strip()
				print h
				a = (block.split("H:\n")[1]).split("A:\n")[1].split("\n")
				print a
				ques.append(Question(q, h, a))
		return ques
	except Exception as e:
		print e
		print "invalid Q file format"


def print_intro():
	print "          ____"
	print "         /.../\\"
	print "        /.../--\\" 
	print "       /.../----\\" 
	print "      /.../------\\"
	print "     /.../---/\---\\" 
	print "    /.../---/\\\\\\---\\"
	print "   /.../---/\\\\\\\\\---\\"
	print "  /.../===/__\\\\\\\\\---\\"
	print " /............\\\\\\\\\---\\"
	print "/..............\\\\\\\\\---\\"
	print "\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\--/"
	print " \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/"

def print_menu():
	print_intro()
	print "\nPuzzle Interface:"
	print "[1] Query question"
	print "[2] Current scores"
	print "[3] Last email"
	print "[4] Test answer\n"

def run():
	num =""
	while (num != "5"):
		os.system("/usr/bin/clear")
		print_menu()
		num = int(raw_input())
		while (num<1 or num>5):
			os.system("/usr/bin/clear")
			print_menu()
			print "\033[31m	 invalid input \033[0m"
			num = raw_input()
		
		if (num==1):
			query_question()
		elif (num==4):
			test_ans_interactive()
		print "press enter to coninue:"
		raw_input()


#		MAIN METHOD
if __name__ == '__main__':

	id = str(random.randint(1, 100000))
	questions.extend(get_q_from_file("q1.txt"))
	
	try:
		run()
	except KeyboardInterrupt as e:
		exit()