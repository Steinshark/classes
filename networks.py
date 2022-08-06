import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import matplotlib.pyplot as plt
import numpy as np
import math
import random
class FullyConnectedNetwork(nn.Module):
	def __init__(self,input_size,output_size):
		super(FullyConnectedNetwork,self).__init__()

		self.model = nn.Sequential(
			nn.Linear(input_size,64),
			nn.ReLU(),
			nn.Linear(64,16),
			nn.ReLU(),
			nn.Linear(16,output_size))

		self.optimizer = optim.RMSprop(self.model.parameters(),lr=1e-1)


	def train(self,x_input,y_actual,epochs=1000,lr=1e-4,verbose=False,show_steps=10):
		memory = 5
		prev_loss = [100000000 for x in range(memory)]
		losses = []
		for i in range(epochs):
			y_pred = self.forward(x_input)

			criterion = nn.MSELoss()
			loss = criterion(y_pred,y_actual)
			losses.append(loss)

			if not False in [prev_loss[x] > prev_loss[x+1] for x in range(len(prev_loss)-1)]:
				print(f"broke on epoch {i}")
				break
			else:
				prev_loss = [loss] + [prev_loss[x+1] for x in range(len(prev_loss)-1)]

			if verbose and i % show_steps == 0:
				print(f"loss on epoch {i}:\t{loss}")
			self.optimizer.zero_grad()
			loss.backward()
			self.optimizer.step()

	def forward(self,x_list):
		y_predicted = []
		y_pred = self.model(x_list)
		return y_pred
		#	y_predicted.append(y_pred.cpu().detach().numpy())


class ConvolutionalNetwork(nn.Module):
	def __init__(self,input_dimm):
		super(ConvolutionalNetwork,self).__init__()

		self.model = nn.Sequential(
			nn.Linear(input_dimm,64),
			nn.ReLU(),
			nn.Linear(64,8),
			nn.ReLU(),
			nn.Linear(8,4))

		self.loss_function = nn.MSELoss()
		self.optimizer - optim.SGD(self.model.parameters(),lr=1e-4)

	def train(self,x_input,y_actual,epochs=10):

		#Run epochs
		for i in range(epochs):

			#Predict on x : M(x) -> y
			y_pred = self.model(x_input)

			#Find loss  = y_actual - y
			loss = self.loss_function(y_pred,y_actual)
			print(f"epoch {i}:\nloss = {loss}")

			#Update network
			self.optimizer.zero_grad()
			loss.backward()
			self.optimizer.step()

	def forward(self,x):
		return self.model(x)

if __name__ == "__main__":
	function = lambda x : math.sin(x*.01) + 4
	x_fun = lambda x : [x, x**2, 1 / (x+.00000001), math.sin(x * .01)]
	x_train = torch.tensor([[x] for x in range(2000) if random.randint(0,100) < 80],dtype=torch.float)
	x_train1 =  torch.tensor([x_fun(x) for x in range(2000) if random.randint(0,100) < 80],dtype=torch.float)
	y_train = torch.tensor([[function(x[0])] for x in x_train1],dtype=torch.float)

	#print(x_train.shape)
	#print(y_train.shape)
	#plt.scatter(x_train,y_train)
	#plt.show()
	print("Prelim dataset")

	model = FullyConnectedNetwork(len(x_train1[0]))
	model.train(x_train1,y_train)



	x_pred = torch.tensor([[x] for x in range(2000) if random.randint(0,100) < 20],dtype=torch.float)
	x_pred1 = torch.tensor([x_fun(x) for x in range(2000) if random.randint(0,100) < 20],dtype=torch.float)

	y_actual = torch.tensor([[function(x[0])] for x in x_pred1],dtype=torch.float)


	y_pred = model.forward(x_pred1).cpu().detach().numpy()

	plt.scatter([i for i in range(len(x_pred1))],y_actual)
	plt.scatter([i for i in range(len(x_pred1))],y_pred)
	plt.show()
	print("model output")
