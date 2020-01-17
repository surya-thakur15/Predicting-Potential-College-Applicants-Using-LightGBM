

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split


# In[2]:


df = pd.read_csv('D:\CoreProject\ProjectData_50k.csv')



df.apply(lambda x: sum(x.isnull()) )


# In[6]:


df.drop(["Name", "TotalScore"], axis = 1, inplace = True) 


# In[7]:


df.head()


# Categorical boolean mask
categorical_feature_mask = df.dtypes==object


categorical_feature_mask


# filter categorical columns using mask and turn it into a list
categorical_cols = df.columns[categorical_feature_mask].tolist()

# In[12]:

categorical_cols


labelencoder = LabelEncoder()


# In[14]:


df[categorical_cols] = df[categorical_cols].apply(lambda colm: labelencoder.fit_transform(colm))


y = df.iloc[:, -1].values


df.drop(["Age","Admitted"], axis = 1, inplace = True) 


# In[18]:


df.head()


# In[19]:


categorical_feature_mask = df.dtypes==object


# In[20]:


hotencode = OneHotEncoder(categorical_features=categorical_feature_mask, sparse=False)


# In[21]:


X = hotencode.fit_transform(df)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)


# In[24]:


df.shape

###############################################################################################################

# # 1. Predicting results using Logistic Regression

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

model = LogisticRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(model.score(X_test, y_test))

cm = confusion_matrix(y_test, y_pred)
# print(cm)

c_report = classification_report(y_test, y_pred)

print(c_report)


#####################################################################################################################

from sklearn.naive_bayes import GaussianNB


# In[31]:


model = GaussianNB()


# In[32]:


model.fit(X_train, y_train)


# In[33]:


y_pred = model.predict(X_test)


# In[34]:


from sklearn import metrics

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))



#############################################################################################################

# # 3.1. Predicting results using Neural Networks

import keras

from keras import Sequential
from keras.layers import Dense


# In[35]:


classifier = Sequential()


# In[36]:


# First Hidden Layer
classifier.add(Dense(7, activation='relu', kernel_initializer='random_normal', input_dim=13))


# In[37]:


# Second Hidden Layer
classifier.add(Dense(7, activation='relu', kernel_initializer='random_normal'))


# In[38]:


# Third Hidden Layer
classifier.add(Dense(7, activation='relu', kernel_initializer='random_normal'))


# In[39]:


# Fourth Hidden Layer
classifier.add(Dense(7, activation='relu', kernel_initializer='random_normal'))


# In[40]:


#Output Layer
classifier.add(Dense(1, activation='sigmoid', kernel_initializer='random_normal'))


# In[41]:


# Compiling the neural network
classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])


# In[42]:


history = classifier.fit(X, y, validation_split=0.25, batch_size=150, epochs=250)


# In[56]:


print(history.history.keys())



get_ipython().run_line_magic('matplotlib', 'notebook')
loss_train = history.history['loss']
loss_val = history.history['val_loss']
epochs = range(1,251)
plt.plot(epochs, loss_train, 'r', label='Training loss')
plt.plot(epochs, loss_val, 'b', label='validation loss')
plt.title('Training and Validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()


# In[61]:


get_ipython().run_line_magic('matplotlib', 'notebook')
accuracy_train = history.history['accuracy']
loss_val = history.history['val_accuracy']
epochs = range(1,251)
plt.plot(epochs, accuracy_train, 'r', label='Training accuracy')
plt.plot(epochs, loss_val, 'b', label='validation accuracy')
plt.title('Training and validation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

# In[62]:

X_train.shape


# In[63]:


eval_model = classifier.evaluate(X_train, y_train)
print(eval_model)

####################################################################################################################################

import lightgbm as lgb


# In[35]:


d_train = lgb.Dataset(X_train, label=y_train)

# In[36]:

params = {}

params['learning_rate'] = 0.03
params['boosting_type'] = 'gbdt'
params['objective'] = 'binary'
params['metric'] = 'binary_logloss'
params['sub_feature'] = 0.5
params['num_leaves'] = 100
params['min_data'] = 500
params['max_depth'] = 100

# In[37]:

clf = lgb.train(params, d_train, 1000)

#Prediction

y_pred=clf.predict(X_test)
#convert into binary values
for i in range(0,12500):
    if y_pred[i]>=0.5:       # setting threshold to .5
       y_pred[i]=1
    else:  
       y_pred[i]=0


# In[39]:


from sklearn.metrics import accuracy_score
accuracy=accuracy_score(y_pred,y_test)


# In[40]:


print("Accuracy of the model is: ", accuracy)


# In[41]:


from sklearn.metrics import confusion_matrix, classification_report
cm = confusion_matrix(y_test, y_pred)


# In[42]:


print(cm)



c_report = classification_report(y_test, y_pred)


# #### Classfication Report for the LightGBM


print(c_report)





