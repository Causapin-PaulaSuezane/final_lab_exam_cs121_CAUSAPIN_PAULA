import os
from utils.user_manager import UserManager
from utils.score import Score

class DiceGame:
	def __init__(self):
		self.user_manager = UserManager()
		self.scores = []
		self.current_user = None
		self.load_scores()

	def load_scores(self):
		if not os.path.exist('data'):
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

	def play_game():
		pass

	def show_top_scores():
		pass

	def logout():
		pass

	def menu():
		pass