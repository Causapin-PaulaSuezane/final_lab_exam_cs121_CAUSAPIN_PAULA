import os
import random
from utils.user_manager import UserManager
from utils.score import Score

class Dice:
    def roll(self):
        return random.randint(1,6)
    
class DiceGame:
	def __init__(self):
		self.user_manager = UserManager()
		self.scores = []
		self.current_user = None
		self.load_scores()
		self.dice = Dice()
  
	def load_scores(self):
		if not os.path.exists('data'):
			os.makedirs('data')
		if not os.path.exists('data/rankings.txt'):
			open ('data/rankings.txt', 'w').close()

		with open ('data/rankings.txt', 'r') as file:
			for line in file:
				username, points, wins = line.strip().split(',')
				self.scores.append(Score(username, int(points), int(wins)))

	def save_scores(self):
		with open ('data/rankings.txt', 'w') as file:
			for score in self.scores:
				file.write (f"{score.username},{score.points}, {score.wins}\n")

	
	def play_game(self):
		print("\nBest of three rounds!")
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
				print(f"\n{self.current_user} wins te round!\n")
				user_wins += 1
			elif user_roll < cpu_roll:
				print(f"\nCPU wins the round!\n")
				cpu_wins += 1
			else:
				print("\nIts a tie.\n")

		if user_wins > cpu_wins:
			print("\nCongrats! You won!")
			points = 10
			wins = 1
		elif user_wins < cpu_wins:
			print ("\nYou lost. CPU wins this game.")
			points = 0
			wins = 0
		else:
			print("\nIts a tie.")
			points = 0
			wins = 0
	
		for score in self.scores:
			if score.username == self.current_user:
				score.points += points
				score.wins += wins
				break
		else:
			new_score = Score(self.current_user, points, wins)
			self.scores.append(new_score)

		self.save_scores()
  
	def show_top_scores(self):
		print("Top 10 scores : ")
		if not self.scores:
			print("No scores yet.")
			return
		self.scores.sort(key = lambda x: x.points, reverse=True)

		for rank, score in enumerate(self.scores[:10], start = 1):
			if score in self.scores[:10]:
				print(f"{rank}. {score.username}, Points {score.points}, Wins {score.wins}")

	def logout(self):
		self.current_user = None
		print("Logged out.")

	def menu(self):
		print (f"\nWelcome {self.current_user}!!")
		while True:
			try:
				print("\nMenu : ")
				print("1. Start")
				print("2. View Rankings")
				print("3. Log Out")
				choice = int(input("Enter your choice : "))
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