'''
Created on Aug 11, 2015
@author: brandonchoi
'''

# FIRST GO AT PYTHON!

# parser for text file with the following syntax: "first name" [middle name] "last name"
# accounts for middle name being more than 1 word
# ex: 'Homer John Simpson' becomes 'homer.j.simpson@duke.edu'

# code also accomplishes same task for net id's
# ex: 'abc123'  becomes 'abc123@duke.edu'

class Parser(object):
	
	allEmails = []
	domain_address = ''
	
	def _init_(self, file_name, domain_input):
		file = open(file_name, 'r')
		lines = file.read().split('\n')
		self.domain_address = domain_input
		
		for line in lines:
			self.createNameArray(line)
		
	#separates individual's name into array. middle name(s) are made into just their initials
	def createNameArray(self, name):
		name_parts = name.split()
		#abbreviate the middle names
		for part in name_parts:
				if (part != name_parts[0]) and (part != name_parts[len(name_parts) - 1]):
					i = name_parts.index(part)
					name_parts[i] = part[0]
								
		self.addEmail(name_parts)

	#adds the '.' where necessary and appends email address as well					
	def addEmail(self, x):
		email = ('.'.join(x)).lower() + self.domain_address
		self.allEmails.append(email)


#holds instance of Parser and writes out new text file with correct emails
class Emailer():
	file_name = 'practice.txt' #INSERT FILE NAME HERE
	domain_address = '@' + 'duke.edu' #EMAIL DOMAIN
	
	#parser object
	myParser = Parser()
	myParser._init_(file_name, domain_address)
	
	#writes out email addresses
	recipients = myParser.allEmails
	output = open('results.txt', 'w')
	for r in recipients:
		output.write(r + '\n')
	
	#TODO : script to open up mail app and include recipients
	
	
	
	