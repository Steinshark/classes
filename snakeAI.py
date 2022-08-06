import pygame
from random import randint
import random
import time
import pprint
import networks
import json
import numpy as np
import os
import torch

class SnakeGame:

	def __init__(self,w,h,fps=30):
		self.width = w
		self.height = h

		self.food = (randint(0,self.width - 1),randint(0,self.height - 1))
		self.snake = [[0,0]]

		self.colors = {"FOOD" : (255,20,20),"SNAKE" : (20,255,20)}

		self.frame_time = 1 / fps

		self.snapshot_vector = [[0 for x in range(self.height)] for i in range(self.width)]

		self.direction = (1,0)

		self.data = []

	def play_game(self,window_x,window_y,training_match=True,model=None):


		if not window_x == window_y:
			print(f"invalid game_size {window_x},{window_y}.\nDimensions must be equal")
			return

		square_width 	= window_x / self.width
		square_height 	= window_y / self.height


		#Display setup
		pygame.init()
		self.window = pygame.display.set_mode((window_x,window_y))
		pygame.display.set_caption("AI Training!")


		self.output_vector = [0,0,0,1]
		game_running = True

		while game_running:
			self.window.fill((0,0,0))
			pygame.event.pump()
			t_start = time.time()
			keys = pygame.key.get_pressed()


			#print(keys[pygame.K_w])
			f_time = t_start - time.time()

			#Draw snake and food
			if training_match:
				self.update_movement()
				self.create_input_vector()

			else:
				assert model is not None

				y_feed = torch.tensor(self.game_to_model(self.create_input_vector()),dtype=torch.float)
				model_out = model.forward(y_feed)

				w,s,a,d = model_out.cpu().detach().numpy()
				print([w,a,s,d])
				keys= pygame.key.get_pressed()
				if True in [keys[pygame.K_w],keys[pygame.K_a],keys[pygame.K_s],keys[pygame.K_d]]:
					print("overriding ML")
					self.update_movement(player_input=True)
				else:
					self.update_movement(player_input=False,w=w,s=s,a=a,d=d)

			for coord in self.snake:
				x,y = coord[0] * square_width,coord[1] * square_height
				new_rect = pygame.draw.rect(self.window,self.colors["SNAKE"],pygame.Rect(x,y,square_width,square_height))
			x,y = self.food[0] * square_width,self.food[1] * square_height
			food_rect = pygame.draw.rect(self.window,self.colors["FOOD"],pygame.Rect(x,y,square_width,square_height))
			pygame.display.update()


			#Movement
			next_x = self.snake[0][0] + self.direction[0]
			next_y = self.snake[0][1] + self.direction[1]
			if next_x >= self.width or next_y >= self.height or next_x < 0 or next_y < 0:
				game_running = False
			next_head = (next_x , next_y)

			if next_head in self.snake:
				print("you lose!")
				game_running = False

			if next_head == self.food:
				self.food = (randint(0,self.width - 1),randint(0,self.height - 1))
				self.snake = [next_head] + self.snake
			else:
				self.snake = [next_head] + self.snake[:-1]

			if keys[pygame.K_p]:
				print(f"input vect: {self.vector}")
				print(f"\n\noutput vect:{self.output_vector}")
			#Keep constant frametime
			self.data.append({"x":self.input_vector,"y":self.output_vector})
			if self.frame_time > f_time:
				time.sleep(self.frame_time - f_time)


		self.save_data()

	def save_data(self):
		x = []
		y = []
		for item in self.data[:-1]:
			x_item = np.ndarray.flatten(np.array(item["x"]))
			y_item = np.array(item["y"])

			x.append(x_item)
			y.append(y_item)

		x = np.array(x)
		y = np.array(y)

		if not os.path.isdir("experiences"):
			os.mkdir("experiences")

		i = 0
		fname = f"exp_x_{i}.npy"
		while os.path.exists(os.path.join("experiences",fname)):
			i += 1
			fname = f"exp_x_{i}.npy"
		np.save(os.path.join("experiences",fname),x)
		np.save(os.path.join("experiences",f"exp_y_{i}.npy"),y)

	def game_to_model(self,x):
		return np.ndarray.flatten(np.array(x))

	def create_input_vector(self):
		self.input_vector = [[0 for x in range(self.height)] for y in range(self.width)]
		self.input_vector[self.snake[0][1]][self.snake[0][0]] = 1
		for piece in self.snake[1:]:
			self.input_vector[piece[1]][piece[0]] = -1
		food_placement = [[0 for x in range(self.height)] for y in range(self.width)]
		food_placement[self.food[1]][self.food[0]] = 1
		self.input_vector += food_placement
		return self.input_vector

	def update_movement(self,player_input=True,w=0,s=0,a=0,d=0):

		if player_input:
			pygame.event.pump()
			keys = pygame.key.get_pressed()
			w,s,a,d = (0,0,0,0)

			if keys[pygame.K_w]:
				w = 1
			elif keys[pygame.K_s]:
				s = 1
			elif keys[pygame.K_a]:
				a = 1
			elif keys[pygame.K_d]:
				d = 1
			else:
				return
			self.output_vector = [w,s,a,d]

		self.movement_choices = {
			(0,-1) 	: w,
			(0,1) 	: s,
			(-1,0) 	: a,
			(1,0)	: d}

		next_dir = max(self.movement_choices,key=self.movement_choices.get)
		if self.direction[0] - next_dir[0] > 0 and self.direction[1] - next_dir[1] > 0:
			self.movement_choices[next_dir] = 0
			self.direction = max(self.movement_choices,key=self.movement_choices.get)
		else:
			self.direction = next_dir
		print(self.direction)


if __name__ == "__main__":

	import sys
	if sys.argv[1] == "-t":
		s = SnakeGame(20,20,fps=15)
		s.play_game(600,600,training_match=True)
		exit()
	#s = SnakeGame(20,20,fps=20)
	#s.play_game(600,600)

	exp = {}
	x_exp = {}
	y_exp = {}

	for f in os.listdir("experiences"):
		type = f[4]
		number = f[6:].split(".")[0]

		if not number in exp:
			exp[number] = {"x" :None,"y":None}

		if type == "x":
			exp[number]["x"] = np.load(os.path.join("experiences",f))
		else:
			exp[number]["y"] = np.load(os.path.join("experiences",f))

	final_boss_list = {"x":np.empty((0,800)),"y":np.empty((0,4))}
	for num in exp:
		final_boss_list["x"] = np.append(final_boss_list['x'], exp[num]["x"],axis=0)
		final_boss_list["y"] = np.append(final_boss_list['y'], exp[num]["y"],axis=0)



	x_data = torch.from_numpy(final_boss_list["x"]).float()
	y_data = torch.from_numpy(final_boss_list["y"]).float()

	model = networks.FullyConnectedNetwork(800,4)

	print(f"training model on {x_data.shape} datapoints")
	model.train(x_data,y_data,verbose=True,epochs=int(sys.argv[2]),show_steps=50)

	game = SnakeGame(20,20,fps=4)
	game.play_game(600,600,training_match=False,model=model)
