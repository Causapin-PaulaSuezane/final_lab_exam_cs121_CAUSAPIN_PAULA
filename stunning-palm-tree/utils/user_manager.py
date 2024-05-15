import os

class UserManager:
	def __init__(self):
		self.users = {}
		self.load_users()

	def load_users(self):
		if not os.path.exists ('data'):
			os.makedirs ('data')
		if not os.path.exists('data/users.txt'):
			open ('data/users.txt', 'w').close()

		with open ('data/users.txt', 'r') as file:
			for line in file:
				username, password = line.strip().split(',')
				self.users[username] = password

	def save_users(self):
		with open ('data/users.txt', 'w') as file:
			for username, password in self.users.items():
				file.write(f"{username},{password}\n")

	def validate_username(self, username):
		return len(username) >= 4

	def validate_password(self, password):
		return len(password) >=8

	def register(self, username, password):
		if self.validate_username(username and self.validate_password):
			self.username[username] = password
			self.save_users()
			return True
		return False

	def login(self, username, password):
		return self.users.get(username) == password
		pass
