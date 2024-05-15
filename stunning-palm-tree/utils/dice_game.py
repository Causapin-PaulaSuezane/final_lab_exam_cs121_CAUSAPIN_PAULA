import os
import uuid
import random
from utils.user_manager import UserManager
from utils.score import Score


class DiceGame:
	def __init__(self):
		self.user_manager = UserManager()
		self.scores = []
		self.current_user = None
		self.load_scores()
  
	def load_scores(self):
		if not os.path.exists('data'):
			os.makedirs('data')
		if not os.path.exists('data/rankings.txt'):
			open ('data/rankings.txt', 'w').close()

		with open ('data/rankings.txt', 'w') as file:
			for line in file:
				username, game_id, points, wins = line.strip().split(',')
				self.scores.append(Score(username, game_id, int(points), int(wins)))

	def save_scores(self):
		with open ('data/rankings.txt', 'w') as file:
			for score in self.scores:
				file.write (f"{score.username},{score.game_id},{score.points}, {score.wins}\n")

	def play_game(self):
		print("Best of three rounds!")
		print("Game starting...")
		
		user_wins = 0
		cpu_wins = 0

		for round_num in range(1,4):
			input("Press enter to roll the dice...")
			print(f"\nRound {round_num} : ")
   
			self.dice.roll()
			user_roll = random.randint(1,6)
			print(f"{self.current_user} rolled: {user_roll}")
   
			self.dice.roll()
			cpu_roll = random.randint(1,6)
			print(f"CPU rolled: {cpu_roll}")
   
			if user_roll > cpu_roll:
				print(f"{self.current_user} wins te round!")
				user_wins += 1
			elif user_roll < cpu_roll:
				print(f"CPU wins the round!")
				cpu_wins += 1
			else:
				print("Its a tie.")

		if user_wins > cpu_wins:
			print("\nCongrats! You won!")
		elif user_wins < cpu_wins:
			print ("You lost. CPU wins this game.")
		else:
			print("Its a tie.")
   
		if user_wins > cpu_wins:
			points = 10
			wins = 1
		elif user_wins < cpu_wins:
			points = 0
			wins = 0
		else:
			points = 0
			wins = 0
	
		game_id = str(uuid.uuid4())
		new_score = Score(self.current_user, game_id, points, wins)
		self.scores.append(new_score)
		self.save_score()
   
	def show_top_scores(self):
		print("Top 10 scores : ")
		if not self.scores:
			print("No scores yet.")
			return
		self.scores.sort(key = lambda x: x.points, reverse=True)
		for score in self.score:
			print(f"Username : {score.username}, Game ID : {score.game_id}, Points {score.points}, Wins {score.wins}")

	def logout(self):
		self.current_user = None
		print("Logged out.")

	def menu(self):
		print (f"Welcome") # {username}")
		while True:
			try:
				print("Menu : ")
				print("1. Start")
				print("2. View Rankings")
				print("3. Log Out")
				choice = int(input("Enter your choice, or leave blank to cancel : "))
				if choice == 1:
					self.play_game()
					pass
				elif choice == 2:
					self.show_top_scores()
					pass
				elif choice == 3:
					print("Logging out....")
					print("Thanks for playing!")
					self.logout()
					break
				else:
					print("Invalid input.")
			except ValueError:
				print("ValueError. Please input a number within the choices.")