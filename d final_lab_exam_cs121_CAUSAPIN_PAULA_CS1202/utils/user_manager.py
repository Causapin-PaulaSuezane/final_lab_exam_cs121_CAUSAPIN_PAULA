import os

class UserManager:
	def __init__(self):
		self.users = {}
		self.load_users()

#loads the user in the users.txt file
	def load_users(self):
		if not os.path.exists ('data'): #creates data file if it doesnt exists yet
			os.makedirs ('data')
		if not os.path.exists('data/users.txt'):
			open ('data/users.txt', 'w').close()

		with open ('data/users.txt', 'r') as file: #reads the file users.txt
			for line in file:
				username, password = line.strip().split(',')
				self.users[username] = password

#saves the new user to users.txt file
	def save_users(self):
		with open ('data/users.txt', 'w') as file:
			for username, password in self.users.items():
				file.write(f"{username},{password}\n")

#validates/checks if the typed username is >= to 4 characters long
	def validate_username(self, username):
		return len(username) >= 4
#validates/checks if the typed password is >= to 8 characters long
	def validate_password(self, password):
		return len(password) >=8

#register function for new users
	def register(self, username, password):
		if self.validate_username(username) and self.validate_password(password): #for checking its character lengths
			if username not in self.users:
				self.users[username] = password #kambal na ang username at password
				self.save_users() #saves the newly created users in users.txt file
				print("User registered successfully.")
				
			else:
				print("Username already exists.")
		else:
			print("\nInvalid. Username should be >= 4 characters, and password be >= 8 characters. ")
       

	def login(self, username, password):
		if username in self.users: #if typed username exists
			return self.users[username] == password #validates if the username anad password matched (kambal pa ba?)
		else:
			print("Username does not exist.")
   