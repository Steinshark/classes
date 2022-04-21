import pygame
from pygame.locals import *
import random
import math
import pprint 
import numpy
import time 
import sys 
_DATASET = {"X":[],"y":[]}
_VisualSim  	= False
_ShootDownRange = 100
_NetRangeAir 	= 450
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
_White 			= (244,244,255)
_FONT 			= None
_HFONT 			= None


# Unit Size 
_FMAX 			= 50
_EMAX			= 40
_AMAX 			= 5



#Euclidean distance 
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
			return (1 / (10*(dist+2))) < random.uniform(0,1)#Model assumes for every hour.


	#Define the chance of network traffic going through 
	if model=="packet_success":
		global _PCount
		global _PNext
		_PCount += 1
		if dist > _PacketRange:
			return 0
		else:
			p = (_PacketRange - dist) / (_PacketRange + dist) #Assume an exponential dropoff
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


class battlespace:
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

		friendly_circles = [(random.uniform(20 ,(self.w/2) - 1),random.uniform(200,(self.h) - 201)) for _ in range(_FCircles)]

		for unit in self.friendlyGround:
			x,y = friendly_circles[random.randint(0,_FCircles-1)]
			angle = random.uniform(0,360)
			r = random.uniform(0,_SpawnRadius)
			dist  = random.uniform(30,50) + (math.sqrt(_SpawnRadius-r) / math.sqrt(_SpawnRadius))


			unit.x = x + math.cos(r)*dist 
			unit.y = y + math.sin(r)*dist


		enemy_circles = [(random.uniform((self.w/2) - 1, self.w-200),random.uniform(200,(self.h) - 201)) for _ in range(_ECircles)]
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
		self.w,self.h = self.screen.get_size()
		if not sim:
			self.draw_units()
			self.find_networks()
			return
		self.move_units()
		if _VisualSim:
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
						for k in self.networks[u2.net] + self.networks[u1.net]:
							self.networks[new_net].append(k)
							k.net = new_net

						del(self.networks[u2.net])
						del(self.networks[u1.net])

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
						a.intel += ((d - _IntelRange) / _IntelRange)**2
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
				print(f"Nets on aircraft {a}: {len(nets)}")
				c = 0 
				# Check each combination of networks that this aircraft is sponsoring
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
											if euclidean(p1.x,p1.y,p2.x,p2.y) < 50:
												break
										else:
											continue# skip 90% of time 
									c += 1
									d = euclidean(p1.x,p1.y,a.x,a.y) 	#distance of "sender" 
									d2 = euclidean(p2.x,p2.y,a.x,a.y)	#distance of "reciever"

									#Try to send up to 100 packets. Goes through the probability model twice, once for the probability 
									#that the sender gets it to the aircraft, and again for the aircraft getting it to the
									#receiver
									packets_successfully_sent 		=  sum([prob_model("packet_success",d) for _ in range(random.randint(0,100))])
									packets_successfully_recieved 	=  sum([prob_model("packet_success",d2) for _ in range(int(packets_successfully_sent))])
										
									#Update our counts of both the aircraft and of the whole model
									a.packets_handled += packets_successfully_recieved
									self.packets += packets_successfully_recieved
				print(f"\t{c} units communicated")
			#Display the information in the model HUD
			text1 = _HFONT.render(f"Aircraft {a}", True, _White, _Black)
			text2 = _HFONT.render(f"Nets sponsored:\t{len(a.nets)}", True, _White, _Black)
			text3 = _HFONT.render(f"Packets Handled:\t{a.packets_handled}", True, _White, _Black)
			
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

			_DATASET["X"].append(numpy.array(data_list))

	def end_round(self):
		for a in self.friendlyAir:

			# HEURISTIC LOOKS AT 
			#       cost if ded 	number of packets (scaled) 	  	regain cost if alive    Time lived helpful      total networkds bridged  
			score = (-600) 			+ (a.packets_handled/4)**2 	+ (int(not a.ded)*600) 	- (a.hours_lived) 	+ (a.connected/10)
			print(f"{a} scored: {score}")
			_DATASET['y'].append(score)


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

			_HFONT 			= pygame.font.SysFont('arial', 20)

	def run(self):
		t1 = time.time()
		for i in range(self.iterations):
			if i % 100 == 0:
				print(f"finished {i} iterations")
			b = battlespace(self.width,self.height,self.f,self.e,self.a,self.screen)
			b.draw_units()
			pygame.display.flip()

			set_running = False
			hour = 0
			while hour < 100:
				self.width,self.height = self.screen.get_size()
				b.w = width
				b.h = height

				for event in pygame.event.get():
					if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
						pygame.quit()
						exit(0)
					elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
						self.screen.fill(_Black)

						b.compute_environment()
						pygame.display.flip()
						hour += 1
						continue
					elif event.type == pygame.KEYDOWN and event.key == pygame.K_t:
						set_running = not set_running

				if set_running:
					self.screen.fill(_Black)

					b.compute_environment(sim=True)
					pygame.display.flip()
					hour += 1
					continue
			b.end_round()
		print(f"ran {self.iterations} simulations in {(time.time()-t1):.3f} seconds")

	def generateNewBattlespace(self):
		self.width,self.height = self.screen.get_size()
		set_running = False
		b = battlespace(self.width,self.height,self.f,self.e,self.a,self.screen,forSim=False)
		b.compute_environment()
		b.draw_units()
		pygame.display.flip()
		while True:
			self.width,self.height = self.screen.get_size()

			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
					pygame.quit()
					exit(0)
				elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
					self.screen.fill(_Black)

					b.compute_environment(sim=True)
					pygame.display.flip()
					continue
				elif event.type == pygame.KEYDOWN and event.key == pygame.K_t:
					set_running = not set_running

			if set_running:
				self.screen.fill(_Black)

				b.compute_environment(sim=True)
				pygame.display.flip()
				continue




if __name__ == "__main__":

	if False:
		_VisualSim = True
		engine = Engine(1,1920,1080,30,20,2)
		engine.generateNewBattlespace()
		exit(0)

	try:
		width = int(sys.argv[1])
		height = int(sys.argv[2])
		f = int(sys.argv[3])
		if  f > _FMAX:
			print(f"up to {_FMAX} friendlies")
		e = int(sys.argv[4])
		if  e > _EMAX:
			print(f"up to {_EMAX} enemies")
		a = int(sys.argv[5])
		if  a > _AMAX:
			print(f"up to {_AMAX} air units")
		i = int(sys.argv[6])
		v = sys.argv[7] in ['t','T']
	except IndexError:
		print("usage: python sim.py [width] [height] [#friendly_units] [#hostile_units] [#air_assets] [#iterations] [visual (t/f)]")
		exit(1)
	_VisualSim = v
	engine = Engine(i,width,height,f,e,a)
	engine.run()

	if True:
		arrs = []
		for x,y in zip(_DATASET['X'],_DATASET['y']):
			arrs.append(numpy.append(x,y))
		numpy_arr = numpy.array(arrs)
		numpy.save("sim_data1",numpy_arr)




