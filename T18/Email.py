# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.
class Email:
	has_been_read = False

	def __init__(self, email_address, subject_line, email_content):
		self.subject_line = subject_line
		self.email_content = email_content
		self.email_address = email_address


	def mark_as_read(self):
		self.has_been_read = True

	def display_email(self):
		''' Formats and displays email for easy reading '''
		print()
		
		output_string = str('*' * 100)
		output_string += f"\nFrom: \t{self.email_address}"
		output_string += f"\nSubject: {self.subject_line}"
		output_string += str('\n' + '*' * 100)
		output_string += f"\n{self.email_content}"
		output_string += str('\n' + '*' * 100)
		print(output_string)
		
		input("Please press enter to continue")#holds application execution to allow user to read
