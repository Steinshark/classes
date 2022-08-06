#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas 
import numpy
from sklearn.linear_model import LogisticRegression


# Here we will make some initial initializations

# In[2]:


dataframe = pandas.read_csv("data.csv",header=None)
feature_set = [] #find unique features to be one-hot encoded 
new_dataset = [] #beginnings of our final prepared data 


# ## Find all one-hot encoding features 
# 
# Here, we'll go through our data and check all values of features that will need to be one hot encoded. If we find a unique value (i.e. a new member of the discrete set of relationship types)

# In[3]:


for row in dataframe.iterrows():
    datapoint = list(row[1])
    if not datapoint[1] in feature_set:
        feature_set.append(datapoint[1])
    elif not datapoint[3] in feature_set:
        feature_set.append(datapoint[3])
    elif not datapoint[5] in feature_set:
        feature_set.append(datapoint[5])
    elif not datapoint[6] in feature_set:
        feature_set.append(datapoint[6])
    elif not datapoint[7] in feature_set:
        feature_set.append(datapoint[7])
    elif not datapoint[8] in feature_set:
        feature_set.append(datapoint[8])
    elif not datapoint[13] in feature_set:
        feature_set.append(datapoint[13])
        
    # Add to preparing data
    new_dataset.append(datapoint)


# ## Clean and Format the Dataset  

# In[4]:


for i, dp in enumerate(new_dataset):
    
    # initialize a new dict  
    formatted_dp = {}
    # Add manual features 
    formatted_dp["age"] = int(dp[0])
    formatted_dp["fnlwgt"] = int(dp[2])
    formatted_dp["ed_num"] = int(dp[4])
    formatted_dp["gender"] = int((dp[9] == "Male"))
    formatted_dp["capital_gain"] = int(dp[10])
    formatted_dp["capital_loss"] = int(dp[11])
    formatted_dp["hours_per_week"] = int(dp[12])
    formatted_dp["over50k"] = int(dp[-1].strip()[0] == '>')
    
    
    # Add one-hot encoding features 
    for feat in feature_set:
        if feat in dp:
            formatted_dp[feat] = 1
        else:
            formatted_dp[feat] = 0   
    new_dataset[i] = formatted_dp


# ## Data encoding:
# 
# ### Continuous Values 
#     fnlwgt : The final number the census decided on (no idea??)
#     ed_num : No idea what this represents 
#     gender : 0 == male, 1 == female 
#     
# ### One Hot Encoded  
#     Occupation, Race, Country of Origin , Maritial Status, Relationship Status, Familty Status, Education 

# In[5]:


# A look at our dataset
new_dataset[7]


# Now, well compile our data, clean and format it, and turn it into train and test sets - which are numpy arrays

# In[6]:


##### reorder the data correctly since it was in a dict 
ordered_data = []
lengths = {}

for d in new_dataset:  
    
    # Create the datapoint
    classification = d['over50k']
    d_as_l = [d[f] for f in d if not f == 'over50k']
    final_datapoint = [classification] + d_as_l
    
    # Add to our datalist
    ordered_data.append(final_datapoint)

    
# Create a numpy array
data_arr = numpy.array([numpy.array(l) for l in ordered_data])

# Shuffle the data
numpy.random.shuffle(data_arr)
x = int(.8 * len(data_arr))
# Pick 80% for training 
x_train, y_train, x_test, y_test = data_arr[:x,1:], data_arr[:x,0], data_arr[x:,1:], data_arr[x:,0]


# Lets make a logistics model to try to predict with

# In[7]:


# Create a Logistic Classifier for the dataset 
l_model = LogisticRegression(max_iter=100)
l_model.fit(x_train,y_train)


# In[8]:


predicted_val = l_model.predict(x_test)


# In[9]:


cor = 0
tot = 0
for p,a in zip(predicted_val,y_test):
    tot += 1
    if abs(p - a) < .5:
        cor += 1 
print(cor/tot)


# In[ ]:


from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.svm import SVR

# Fit regression model
svr_rbf = SVR(kernel="rbf", C=100, gamma=0.1, epsilon=0.1)
svr_lin = SVR(kernel="linear", C=100, gamma="auto")
svr_poly = SVR(kernel="poly", C=100, gamma="auto", degree=3, epsilon=0.1, coef0=1)

# linear kernel computation
train = numpy.dot(x_train, x_train.T)
svr_rbf.fit(train, y_train)
svr_lin.fit(train, y_train)
svr_poly.fit(train, y_train)

# predict on training examples
test = np.dot(x_test, x_train.T)
print(svr_rbf.predict(test))
print(svr_lin.predict(test))
print(svr_poly.predict(test))


# In[ ]:




