from turtle import Turtle

Y_COR = 20


class ScoreBoard(Turtle):
	def __init__(self, x_cor):
		super().__init__()
		self.color("white")
		self.penup()
		self.hideturtle()
		self.x_cor = x_cor
		self.score = 0
		self.update_score()

	def update_score(self):
		self.clear()
		self.goto(self.x_cor, Y_COR)
		self.write(self.score, align = "center", font = ("Courier", 60, "normal"))

	def score_point(self):
		self.score += 1
		self.update_score()
