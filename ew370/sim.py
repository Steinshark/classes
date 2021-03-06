import pygame
from pygame.locals import *
import random
import math
import pprint 
import numpy
import time 
import sys 
import os
from numba import jit
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

_DATASET = {"X_com":[],"y_com":[],"X_kill":[],"y_kill":[]}
_VisualSim  	= False
_ShootDownRange = 100
_NetRangeAir 	= 350
_NetRangeGround = 100
_PacketRange	= 100
_PCount			= 0
_PNext			= random.randint(20,300)
_SpawnRadius	= 300
_GroundRange	= 200
_EnemyRange 	= 100
_FCircles		= 6 
_ECircles 		= 10
_IntelRange		= 100

# COLORS 
_Blue 			= (45,100,244)
_Green			= (55,255,100)
_Red 			= (244,100,100)
_Black			= (0,0,0)
_DGRAY			= (25,25,30)
_White 			= (244,244,255)
_FONT 			= None
_HFONT 			= None


# Unit Size 
_FMAX 			= 50
_EMAX			= 40
_AMAX 			= 5



#Euclidean distance 
@jit
def euclidean(my_x,my_y,x,y):
	d_x = my_x - x
	d_y = my_y - y 
	return math.sqrt(d_x**2+d_y**2)

def prob_model(model,dist):

	#Define the chance of shootdown prob
	if model=="shootdown":
		if dist > _ShootDownRange:
			return False
		else:
			return random.uniform(0,.024) + (1 / (10*(dist+2))) < random.uniform(0,1)#Model assumes for every hour.


	#Define the chance of network traffic going through 
	if model=="packet_success":
		global _PCount
		global _PNext
		_PCount += 1
		if dist > _NetRangeAir:
			return 0
		else:
			p = random.uniform(.05,.15) + (_NetRangeAir - dist) / (_NetRangeAir + dist) #Assume an exponential dropoff
			#Just cause
			if _PCount % _PNext == 0:
				_PNext = random.randint(20,300)
				_PCount = 0
				d_p = 1 - p 
				p = 1

			return int(random.uniform(0,1) < p)

class airAsset:
	def __init__(self,name,x,y):
		self.name = name
		self.x 					= x 
		self.y 					= y 
		self.hours_lived 		= 0
		self.ded 				= False 
		self.connections 		= 0
		self.packets_handled 	= 0 
		self.peers 			 	= []
		self.nets 		 	  	= []
		self.connected			= 0
		self.intel     			= 0
		self.damage_contribution = 0
	def dist_to(self,unit):
		x,y = unit 
		return math.sqrt((self.x-x)**2 + (self.y-y)**2 ) 

	def dropoff_model(self,max_r,dist):
		a = math.sqrt(max_r-dist)
		return a * (1/a) 

	def __repr__(self):
		return f"({self.x},{self.y})"


class groundAsset:
	def __init__(self,name,x,y):
		self.x = x 
		self.y = y 
		self.net = None
		self.text = None
		self.rect = None
	def find_net_peers(self,peers):
		for p in peers:
			if euclidean(self.x,self.y,p.x,p.y) < _NetRangeGround:
				self.net_peers.add(p)
	def __repr__(self):
		return(f"({int(self.x)},{int(self.y)})-{self.net}")


class enemyAsset:
	def __init__(self,name,x,y):
		self.name = name 
		self.x = x 
		self.y = y
		self.spotted = False
		self.mark = False


class Battlespace:
	def __init__(self,w,h,f_units,e_units,air_units,screen,forSim=True):
		self.friendlyGround = [groundAsset(f"f{i}",0,0) for i in range(f_units)]
		self.enemy 			= [enemyAsset(f"e{i}",0,0) for i in range(e_units)]
		self.friendlyAir	= [airAsset(f"a{i}",random.randint(50,w-200),random.randint(50,h-200)) for i in range(air_units)]
		self.w  			= w 
		self.h   			= h 
		self.networks 		= {} 
		self.screen			= screen
		self.simulating 	= forSim 
		self.hour  			= 0
		self.packets 		= 0
		self.set_units()

		if forSim:
			self.init_data()
		else:
			self.friendlyAir = []

	def set_units(self):

		friendly_circles = [(random.uniform(20 ,(self.w/1.4) - 1),random.uniform(200,(self.h) - 201)) for _ in range(_FCircles)]

		for unit in self.friendlyGround:
			x,y = friendly_circles[random.randint(0,_FCircles-1)]
			angle = random.uniform(0,360)
			r = random.uniform(0,_SpawnRadius)
			dist  = random.uniform(30,50) + (math.sqrt(_SpawnRadius-r) / math.sqrt(_SpawnRadius))


			unit.x = x + math.cos(r)*dist 
			unit.y = y + math.sin(r)*dist


		enemy_circles = [(random.uniform((self.w/3) - 1, self.w-200),random.uniform(200,(self.h) - 201)) for _ in range(_ECircles)]
		for enemy in self.enemy:
			x,y = enemy_circles[random.randint(0,_ECircles-1)]
			angle = random.uniform(0,360)
			r = random.uniform(0,_SpawnRadius)
			dist  = math.sqrt(_SpawnRadius-r) / math.sqrt(_SpawnRadius)

			enemy.x = x + math.cos(r)*dist 
			enemy.y = y + math.sin(r)*dist	

	def move_units(self):

		for unit in self.friendlyGround:
			angle = random.uniform(0,6.28)

			r = random.uniform(0,_GroundRange)
			dist  = random.randint(10,20) + math.sqrt(_GroundRange-r) / math.sqrt(_GroundRange)

			unit.x = unit.x + math.cos(angle)*dist 
			unit.y = unit.y + math.sin(angle)*dist


			if unit.x > self.w:
				unit.x = self.w - 10
			if unit.x < 0: 
				unit.x = 10 
			if unit.y > self.h:
				unit.y = self.h - 10
			if unit.y < 0:
				unit.y = 10 


		for enemy in self.enemy:
			angle = random.uniform(0,6.28)

			r = random.uniform(0,_EnemyRange)
			dist  = random.randint(10,20) + math.sqrt(_EnemyRange-r) / math.sqrt(_EnemyRange)

			enemy.x += math.cos(angle)*dist 
			enemy.y += math.sin(angle)*dist	

			if enemy.x > self.w:
				enemy.x = self.w - 10
			if enemy.x < 0: 
				enemy.x = 10 
			if enemy.y > self.h:
				enemy.y = self.h - 10
			if enemy.y < 0:
				enemy.y = 10 

	def compute_environment(self,sim=True):
		self.hour += 1
		self.move_units()
		if _VisualSim:
			self.w,self.h = self.screen.get_size()
			self.draw_units()
		self.find_networks()
		self.simulate_scene()

	def draw_units(self):

		text = _HFONT.render(str(self.hour), True, _White, _Black)
		rect = text.get_rect()
		rect.center = (50, 20)
		self.screen.blit(text,rect)

		for f in self.friendlyGround:
			pygame.draw.circle(self.screen,_Blue,(f.x,f.y),2)
			f.text = _FONT.render(f"{f}", True, _White, _Black)
			f.rect = f.text.get_rect()
			f.rect.center = (f.x + 5, f.y - 10)
			self.screen.blit(f.text,f.rect)

		for e in self.enemy:
			pygame.draw.circle(self.screen,_Red,(e.x,e.y),2)

		for a in self.friendlyAir:
			if a.ded:
				continue
			pygame.draw.circle(self.screen,_Green,(a.x,a.y),3)

	def find_networks(self):
		self.networks = {}
		for i in range(len(self.friendlyGround)):
			self.friendlyGround[i].net = None

		#CONNECT GROUND NETS VIA GROUND
		networks_2 = []
		for i in range(len(self.friendlyGround)):

			for j in range(i+1,len(self.friendlyGround)):
				u1 = self.friendlyGround[i]
				u2 = self.friendlyGround[j]
				
				if not u1 == u2 and (euclidean(u1.x,u1.y,u2.x,u2.y) < _NetRangeGround):
					#Draw the net conection
					if _VisualSim:
						pygame.draw.line(self.screen,_Blue,(u1.x,u1.y),(u2.x,u2.y))
					
					#Neither has a network. Make a new one 
					if u1.net == None and u2.net == None:
						h = 0
						while h in self.networks:
							h += 1
						new_net = h 
						self.networks[new_net] = [u1,u2]
						u1.net = new_net
						u2.net = new_net
						continue

					elif u1.net in self.networks and (u2.net == None):
						self.networks[u1.net].append(u2)
						u2.net = u1.net
						continue 

					elif (u1.net == None) and u2.net in self.networks:
						self.networks[u2.net].append(u1)
						u1.net = u2.net  

					elif (not (u1.net == None)) and (not (u2.net == None)) and (not (u1.net == u2.net)):
						new_net = 0
						while new_net in self.networks:
							new_net += 1

						self.networks[new_net] = []
						old_1 = u1.net 
						old_2 = u2.net 
						for k in self.networks[old_1] + self.networks[old_2]:
							self.networks[new_net].append(k)
							k.net = new_net

						del(self.networks[old_1])
						del(self.networks[old_2])

		for i in self.friendlyGround:
			if i.net is None:
				new_net = 0 
				while new_net in self.networks:
					new_net += 1 
				i.net = new_net
				self.networks[new_net] = [i]

		#CONNECT GROUND NETS VIA AIR
		for a in self.friendlyAir:

			if a.ded:
				continue

			for u in self.friendlyGround:
				if euclidean(a.x,a.y,u.x,u.y) < _NetRangeAir:

					if _VisualSim:
						pygame.draw.line(self.screen,_Green,(a.x,a.y),(u.x,u.y))
					a.peers.append(u)


					if not u.net in a.peers:
						a.nets.append(u.net)

			if len(a.peers) > a.connected:
				a.connected = len(a.peers)

	def simulate_scene(self):

		tab = 100

		#Kill and spot via ground units
		for f in self.friendlyGround:
			for e in self.enemy:
				d = euclidean(f.x,f.y,e.x,e.y)
				if d < 40:
					e.spotted = True
					if d < 10:
						if (random.uniform(.3,.4)+(len(self.networks[f.net])/15) > .5):
							e.mark = True 
							for a in self.friendlyAir:
								if f in a.peers:
									a.damage_contribution += 40
		self.enemy = [e for e in self.enemy if not e.mark]

		for a in self.friendlyAir:

			#Do nothing if ded
			if a.ded:
				continue
			#Calc if not 
			else:
				a.hours_lived += 1

				#Check if this unit will be show down 
				for e in self.enemy:
					d = euclidean(a.x,a.y,e.x,e.y)

					if d < _IntelRange:
						a.intel += ((random.randint(5,100) + (d - _IntelRange)) / _IntelRange)**2
						if not e.spotted:
							e.spotted = True 
							a.intel += 20
					#Check for shootdown
					if prob_model("shootdown",d):
						a.ded = True
						break 
				
				# Calculate the network traffic on this aircraft

				#The model assumes that each individual on one network has an equal likelihood of contacting every other individual in 
				#Every other network that the air unit is sponsoring

				# Find nets that this aircraft sponsors 
				nets = []
				for n in self.networks:
					if n in a.nets:
						nets.append(self.networks[n])
				c = 0 
				# Check each combination of networks that this aircraft is sponsoring
				distances = {}
				for n1 in nets:
					for n2 in nets:

						if not n1 == n2: # make sure theyre not the same network

							#And for each combination of 1 unit to another other unit in each respective network 
							#Simulate their network traffic
							for p1 in n1:
								for p2 in n2:

									# Probability of a unit contacting another in a diff network is 10% per hour
									if random.uniform(0,1) > .1:
										# If friendly is within 50 of enemy, they certainly will communicate
										for e in self.enemy:
											if euclidean(p1.x,p1.y,e.x,e.y) < 50:
												break 
										else:
											continue# skip 90% of time 
									c += 1
									'''
									if not f"{p1}{a}" in distances:
										d = euclidean(p1.x,p1.y,a.x,a.y) 	#distance of "sender" 
										distances[f"{p1}{a}"] = d 
									else:
										d = distances[f"{p1}{a}"]
									if not f"{p2}{a}" in distances:
										d2 = euclidean(p2.x,p2.y,a.x,a.y)	#distance of "reciever"
										distances[f"{p2}{a}"] = d2
									else:
										d2 = distances[f"{p2}{a}"]
									'''
									d = euclidean(p1.x,p1.y,a.x,a.y)
									d2 = euclidean(p2.x,p2.y,a.x,a.y)

									#Try to send up to 100 packets. Goes through the probability model twice, once for the probability 
									#that the sender gets it to the aircraft, and again for the aircraft getting it to the
									#receiver
									traffic = [prob_model("packet_success",d) for _ in range(random.randint(50,100))]
									packets_successfully_sent 		=  sum(traffic)
									
									packets_successfully_recieved 	=  sum([prob_model("packet_success",d2) for _ in range(int(packets_successfully_sent))])
									#Update our counts of both the aircraft and of the whole model
									a.packets_handled += packets_successfully_recieved
									self.packets += packets_successfully_recieved
			if not  _VisualSim:
				continue 	 
			#Display the information in the model HUD
			text1 = _HFONT.render(f"Aircraft {a}", True, _White, _Black)
			text2 = _HFONT.render(f"Nets sponsored:{len(a.nets)}", True, _White, _Black)
			text3 = _HFONT.render(f"Packets Handled:{a.packets_handled}", True, _White, _Black)
			
			rect1 = text1.get_rect()
			rect2 = text2.get_rect()
			rect3 = text3.get_rect()

			rect1.left = tab

			rect2.left = tab 
			rect2.top  = 20 
			rect3.left = tab
			rect3.top  = 40
			self.screen.blit(text1,rect1)
			self.screen.blit(text2,rect2)
			self.screen.blit(text3,rect3)

			tab += 200

	def init_data(self):
		for a in self.friendlyAir:
			data_list = []
			for f in range(_FMAX):
				if f < len(self.friendlyGround):
					unit = self.friendlyGround[f]
					data_list.append(unit.x)
					data_list.append(unit.y)
					data_list.append(euclidean(unit.x,unit.y,a.x,a.y))
				else:
					data_list.append(0)
					data_list.append(0)
					data_list.append(0)

			for f in range(_EMAX):
				if f < len(self.enemy):
					unit = self.enemy[f]
					data_list.append(unit.x)
					data_list.append(unit.y)
					data_list.append(euclidean(unit.x,unit.y,a.x,a.y))

				else:
					data_list.append(0)
					data_list.append(0)
					data_list.append(0)

			unit = a
			data_list.append(unit.x)
			data_list.append(unit.y)

			_DATASET["X_kill"].append(numpy.array(data_list))
			_DATASET["X_com"].append(numpy.array(data_list))

	def end_round(self):
		for a in self.friendlyAir:

			# HEURISTIC LOOKS AT 
			#       cost if ded 	number of packets (scaled) 	  	regain cost if alive    Time lived helpful      total networkds bridged  
			score = (-600) 			+ (a.packets_handled/1000)**1.5 	+ (int(not a.ded)*600) 	- (a.hours_lived) 	+ (a.connected/10)
			d2e_score = 3*a.intel + a.damage_contribution - 300 + (int(not a.ded)*600)
			
			_DATASET['y_kill'].append(d2e_score)
			_DATASET['y_com'].append(score)

	def generate_model_input(self,interpolationX=20,interpolationY=20):

		self.domain_width = interpolationX
		self.domain_height = interpolationY

		self.datapoints = {}

		print(f"generating data along x: {self.w} and y: {self.h}")
		x_ticks = [(interpolationX/2) + x_div*interpolationX for x_div in range(int(self.w/interpolationX))]
		y_ticks = [(interpolationY/2) + y_div*interpolationY for y_div in range(int(self.h/interpolationY))]

		for x in x_ticks:
			for y in y_ticks:

				new_datapoint = []

				for f in range(_FMAX):
					if f < len(self.friendlyGround):

						unit = self.friendlyGround[f]
						new_datapoint.append(unit.x)
						new_datapoint.append(unit.y)
						new_datapoint.append(euclidean(unit.x,unit.y,x,y))
					else:
						new_datapoint.append(0)
						new_datapoint.append(0)
						new_datapoint.append(0)

				for f in range(_EMAX):
					if f < len(self.enemy):

						unit = self.enemy[f]
						new_datapoint.append(unit.x)
						new_datapoint.append(unit.y)
						new_datapoint.append(euclidean(unit.x,unit.y,x,y))

					else:
						new_datapoint.append(0)
						new_datapoint.append(0)
						new_datapoint.append(0)

				new_datapoint.append(x)
				new_datapoint.append(y)

				self.datapoints[(x,y)] = numpy.array(new_datapoint)


class Engine:
	def __init__(self,i,w,h,f,e,a):
		global _FONT
		global _HFONT
		self.iterations = i
		self.width = w
		self.height = h
		self.screen = None
		self.f = f
		self.e = e 
		self.a = a 

		# engine components
		if _VisualSim:
			options = pygame.RESIZABLE
			self.engine = pygame.init()
			self.screen = pygame.display.set_mode((self.width,self.height),options) 
			_FONT 			= pygame.font.SysFont('arial', 10)
			pygame.display.set_caption('Battlefield Simulation v0.1')

			_HFONT 			= pygame.font.SysFont('arial', 20)

		self.battlespace = Battlespace(self.width,self.height,self.f,self.e,self.a,self.screen)


	def run(self):
		t1 = time.time()
		for i in range(self.iterations):
			if i % 100 == 0:
				print(f"finished {i} iterations")
			b = Battlespace(self.width,self.height,self.f,self.e,self.a,self.screen)
			b.draw_units()
			pygame.display.flip()

			set_running = False
			hour = 0
			while hour < 100:
				self.width,self.height = self.screen.get_size()
				b.w = self.width
				b.h = self.height

				for event in pygame.event.get():
					if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
						pygame.quit()
						exit(0)
					elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
						self.screen.fill(_Black)

						b.compute_environment()
						pygame.display.flip()
						hour += 1
						if len([True for a in b.friendlyAir if not a.ded]) == 0:
							hour = 100
						continue
					elif event.type == pygame.KEYDOWN and event.key == pygame.K_t:
						set_running = not set_running

				if set_running:
					self.screen.fill(_Black)

					b.compute_environment(sim=True)
					pygame.display.flip()
					hour += 1
					if len([True for a in b.friendlyAir if not a.ded]) == 0:
						hour = 100
					continue
			b.end_round()
		print(f"ran {self.iterations} simulations in {(time.time()-t1):.3f} seconds")

	def generateTrainingData(self):
		t1 = time.time()
		avg = 0 
		for i in range(self.iterations):
			if i % 100 == 0:
				dt = time.time()-t1
				avg += dt 
				print(f"finished {i} iterations in {(dt):.3f} - avg {(avg/(i+1)):.3f}")
				t1 = time.time()
			b = Battlespace(self.width,self.height,self.f,self.e,self.a,self.screen)
			hour = 0
			while hour < 100:
				b.compute_environment()
				hour += 1
				if len([True for a in b.friendlyAir if not a.ded]) == 0:
					hour = 100
			b.end_round()
		print(f"ran {self.iterations} simulations in {(time.time()-t1):.3f} seconds")

	def generateNewBattlespace(self):
		self.width,self.height = self.screen.get_size()
		set_running = False
		self.battlespace.compute_environment()
		self.battlespace.draw_units()
		pygame.display.flip()
		while True:
			self.width,self.height = self.screen.get_size()
			self.battlespace.w = self.width 
			self.battlespace.h = self.height
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
					pygame.quit()
					exit(0)
				elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
					self.screen.fill(_DGRAY)

					self.battlespace.compute_environment(sim=True)
					pygame.display.flip()
					continue
				elif event.type == pygame.KEYDOWN and event.key == pygame.K_t:
					set_running = not set_running

				elif event.type == pygame.KEYDOWN and event.key == pygame.K_c:
					self.battlespace.generate_model_input()
					self.predict_for_Battlespace(method="com")
					pygame.display.flip()
					continue
				elif event.type == pygame.KEYDOWN and event.key == pygame.K_k:
					self.battlespace.generate_model_input()
					self.predict_for_Battlespace(method="kill")
					pygame.display.flip()
					continue
			if set_running:
				self.screen.fill(_DGRAY)

				self.battlespace.compute_environment(sim=True)
				pygame.display.flip()
				continue

	def construct_predictive_model(self,data_folder="data"):
		print(f"developing models")

		kill_data = None
		com_data = None

		# Load pre_computed data into one array 
		for file in os.listdir(data_folder):
			if file[-4:] == '.npy':
				if "kill" in file:	
					if kill_data is None:
						kill_data = numpy.load(os.path.join(data_folder,file))
					else:
						new_r = numpy.load(os.path.join(data_folder,file))
						kill_data = numpy.row_stack((kill_data,new_r))
				elif "com" in file:
					if com_data is None:
						com_data = numpy.load(os.path.join(data_folder,file))
					else:
						com_data = numpy.row_stack((com_data,numpy.load(os.path.join(data_folder,file))))				

		#Grab all the data
		kill_data_X = kill_data[:,:-1]
		kill_data_y = kill_data[:,-1]
		com_data_X  = com_data[:,:-1]
		com_data_y  = com_data[:,-1]

		input_dim 	= len(kill_data_X[0])
		output_dim 	= 1

		# Here we build a 3 x hidden layer deep neural network to learn the patterns
		self.kill_model=tf.keras.Sequential([
		  	tf.keras.layers.Dense(input_dim,activation='relu'),
			tf.keras.layers.Dense(100,activation='relu'),
			tf.keras.layers.Dense(10,activation='relu'),
			tf.keras.layers.Dense(10,activation='relu'),
		  	tf.keras.layers.Dense(output_dim)
		  ])

		self.com_model=tf.keras.Sequential([
		  	tf.keras.layers.Dense(input_dim,activation='relu'),
			tf.keras.layers.Dense(100,activation='relu'),
			tf.keras.layers.Dense(10,activation='relu'),
			tf.keras.layers.Dense(10,activation='relu'),
		  	tf.keras.layers.Dense(output_dim)
		  ])

		self.kill_model.compile(optimizer='adam',loss=tf.keras.losses.MeanSquaredError(),metrics=['MSE'])
		self.com_model.compile(optimizer='adam',loss=tf.keras.losses.MeanSquaredError(),metrics=['MSE'])

 	
 		#Train the kill model 
		print(f"Training Kill model")
		t1 = time.time()
		self.kill_model.fit(kill_data_X,kill_data_y,
		    validation_split=.25, #auto train/test splitting...
		    callbacks=[tf.keras.callbacks.EarlyStopping(restore_best_weights=True,patience=4)],
		    epochs=4,
		    verbose=1)
		print(f"trained model in {(time.time()-t1):.3f}s\nTraining com model")

		#Train the com model
		t1 = time.time()
		self.com_model.fit(com_data_X,com_data_y,
		    validation_split=.25, #auto train/test splitting...
		    callbacks=[tf.keras.callbacks.EarlyStopping(restore_best_weights=True,patience=4)],
		    epochs=4,
		    verbose=1)
		print(f"trained model in {(time.time()-t1):.3f}s")	

	def predict_for_Battlespace(self,method="com"):
		# Get input vectors of potential air_assets 
		self.battlespace.generate_model_input()

		# Prepare the rectangles with predictions 
		self.battlespace.air_domains = {}

		# Track for color scheming 
		max_score = 0
		min_score = 0

		# Generate a prediction for each potential air asset location
		input_vectors = []

		# Collect all input vectors of this battlespace 
		for location in self.battlespace.datapoints:
			x,y = location

			input_vectors.append(numpy.array([self.battlespace.datapoints[location]]))
			# Find the location and score values for this domain 
			x_anch,y_anch,width,height = (x-(self.battlespace.domain_width/2),y-(self.battlespace.domain_height/2),self.battlespace.domain_width,self.battlespace.domain_height)
			self.battlespace.air_domains[x,y] = {"rect":(x_anch,y_anch ,width,height),"score":0}	
		

		# Predict on all vectors
		if method == 'com':
			output_vectors = self.com_model.predict(numpy.array(input_vectors))
		elif method == 'kill':
			output_vectors = self.kill_model.predict(numpy.array(input_vectors))

		# Add to model
		for i,location in enumerate(self.battlespace.datapoints):
			x,y = location
			predicted_score = output_vectors[i]
			self.battlespace.air_domains[x,y]["score"] = predicted_score 

			# update vals
			if predicted_score < min_score:
				min_score = predicted_score
			elif predicted_score > max_score:
				max_score = predicted_score

		# Draw model
		for loc in self.battlespace.air_domains:
			rect_tuple = self.battlespace.air_domains[loc]['rect']
			score = self.battlespace.air_domains[loc]['score']

			# Create the image repr of the domain
			s = pygame.Surface((rect_tuple[2],rect_tuple[3]), pygame.SRCALPHA)   # per-pixel alpha

			# Find color 
			if score < 0:
				r_val = 255 * (score / min_score)
				g_val = 55 
				b_val = 55

			elif score > 0:
				r_val = 25
				g_val = (55 * (score / max_score)) + 200
				b_val = 25
			s.fill((r_val,g_val,b_val,150))                    
			self.screen.blit(s, (rect_tuple[0],rect_tuple[1]))


if __name__ == "__main__":
	if sys.argv[1] == "simulate":
		_VisualSim = True
		engine = Engine(100,1920,1080,30,20,3)
		engine.run()
	elif sys.argv[1] == "collect":
		n = int(input("n_iters: "))
		for f_units in [5,10,15,20,25,30]:
			for e_units in [5,10,15,20]:
				print(f"calculating {f_units}, {e_units}:")
				engine = Engine(n,1920,1080,f_units,e_units,3)
				engine.generateTrainingData()
		
		# Save the battelspace comm data 
		arrs_com = []
		for x,y in zip(_DATASET['X_com'],_DATASET['y_com']):
			arrs_com.append(numpy.append(x,y))

		# Save the D2E sequence data 
		arrs_kill = []
		for x,y in zip(_DATASET['X_kill'],_DATASET['y_kill']):
			arrs_kill.append(numpy.append(x,y))	


		np_com = numpy.array(arrs_com)
		np_kill = numpy.array(arrs_kill)

		dir_name = 0 
		while f"com_data{dir_name}.npy" in os.listdir("data"):\
			dir_name += 1
		numpy.save(os.path.join("data", f"com_data{dir_name}.npy"),np_com)

		dir_name = 0
		while f"kill_data{dir_name}.npy" in os.listdir("data"):\
			dir_name += 1
		numpy.save(os.path.join("data", f"kill_data{dir_name}.npy"),np_kill)


	elif sys.argv[1] == "predict":
		_VisualSim = True
		f = 30 
		e = 20 
		a = 1 
		engine = Engine(2000,800,600,f,e,a)
		engine.construct_predictive_model()
		engine.generateNewBattlespace()



