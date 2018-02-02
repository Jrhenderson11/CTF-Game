import re
import imaplib
mail = imaplib.IMAP4_SSL('imap.gmail.com')

game_id = "TEST_ID"
quit = False

def set_id(new_id):
	game_id = new_id

def setup():
	(user, password) = get_login_details("login2.txt")
	print user
	print password
	login(user, password)
	check_emails()

def get_login_details(fname):
	file = open(fname, 'r')
	lines = file.readlines()
	user = lines[0].strip()
	password = lines[1].strip()
	
	file.close()
	return (user, password)
	
def login(user, password):
	mail.login(user, password)

def get_ids():
	mail.list()
	# Out: list of "folders" aka labels in gmail.
	mail.select("inbox") # connect to inbox.
	result, data = mail.search(None, "ALL")
	ids = data[0] # data is a list.
	return ids

def check_emails():
	ids = get_ids()
	print ids
	id_list = ids.split() # ids is a space separated string
	latest_email_id = id_list[-1] # get the latest
	for id in id_list:
		result, data = mail.fetch(id, "(RFC822)") # fetch the email body (RFC822) for the given ID

		raw_email = data[0][1] # here's the body, which is raw text of the whole email
		# including headers and alternate payloads
		
		#try:	
		if "FROM: " in raw_email:
			fromline = re.findall(r'FROM: .*\n', str(raw_email))[0]
			sender = re.findall(r' .*\n', fromline)[0][1:]
		else:
			fromline = re.findall(r'From: .*\n', str(raw_email))[0]
			print fromline
			sender = re.findall(r'(?<=<).*(?=>)',fromline)[0]
		subline = re.findall(r'Subject: .*\n', str(raw_email))[0]
		subject = re.findall(r' .*\n', subline)[0][1:]
		print sender
		print subject
		print "-----------"


def loop(time):
	last_id = 0
	while not quit:
		ids = get_ids()
		if len(ids) > last_id:
			print stuff
		sleep(time)

setup()