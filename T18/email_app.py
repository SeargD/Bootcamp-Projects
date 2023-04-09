### --- OOP Email Simulator --- ###

from Email import Email

# --- Lists --- #
email_inbox = list()

# --- Functions --- #
def populate_inbox():
	''' Adds sample emails to inbox '''
	email_inbox.append(Email("welcome@hyperiondev.com", "Welcome to HyperionDev!", "Hi,\nThis is sample email text\nKind Regards,\nThe Sender"))
	email_inbox.append(Email("support@hyperiondev.com", "Great work on the bootcamp!", "Hi,\nThis is Sample email 2\nKind Regards,\nThe Sender"""))
	email_inbox.append(Email("support@hyperiondev.com", "Your excellent marks!", "Hi,\nThis is Your 3rd sample email\nKind Regards,\nThe Sender"))

def list_emails():
	''' Outputs list of ALL emails in inbox '''
	for count, email in enumerate(email_inbox):
		print(count, email.subject_line)

	print()

def list_unread():
	''' Outputs list of ONLY unread emails '''
	for count, email in enumerate(email_inbox):
		if email.has_been_read == True: #skips read emails
			continue
	
		print(count, email.subject_line) #outputs index and subject line of unread mail
	
	print()

def read_email(index):
	curr_email = email_inbox[index] #Reference to email being read for code readability

	# Create a function which displays a selected email.
	curr_email.display_email()
	# Once displayed, call the class method to set its 'has_been_read' variable to True.
	curr_email.mark_as_read()
	print(f"Email {index} from {curr_email.email_address} marked as read.")

# --- Email Program --- #

populate_inbox()

while True:
	user_choice = int(input('''\nWould you like to:
	1. Read an email
	2. View unread emails
	3. Quit application

	Enter selection: '''))

	if user_choice == 1:
		print()
		list_emails()
		email_to_read = int(input("Please select the email you wish to read: "))
		read_email(email_to_read)

	elif user_choice == 2:
		print("Your unread emails are as follows:\n\n")
		list_unread()
		input("Press enter to contine") #Interrupts program to allow user to read list

	elif user_choice == 3:
		# Quit the application
		print("\nThanks for using the email app. Bye.")
		quit()

	else:
		print("Oops - incorrect input.")

