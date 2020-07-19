#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


dataset = pd.read_csv('webserverlog.csv')


# In[3]:


dataset


# In[4]:


newdata = dataset.drop(['Log Name' , 'Time Zone' , 'Method' , 'Referer' , 'Bytes Sent', 'User Agent'], axis=1)


# In[5]:


newdata


# In[6]:


from sklearn.preprocessing import OneHotEncoder, LabelEncoder


# In[7]:


X = newdata.iloc[:,:]


# In[8]:


x = X.to_numpy()


# In[9]:


x


# In[10]:


label = LabelEncoder()


# In[11]:


IP = label.fit_transform(x[:,0])


# In[12]:


IP


# In[13]:


Date = label.fit_transform(x[:,1])


# In[14]:


Date


# In[15]:


URL = label.fit_transform(x[:,2])


# In[16]:


RC = label.fit_transform(x[:,3])


# In[17]:


df1 = pd.DataFrame(IP, columns=['IP'])


# In[18]:


df2 = pd.DataFrame(Date, columns=['DATE'])


# In[19]:


df3 = pd.DataFrame(URL, columns=['URL'])


# In[20]:


df4 = pd.DataFrame(RC, columns=['Response Code'])


# In[21]:


frames = [df1, df2, df3, df4]


# In[22]:


result = pd.concat(frames, axis=1 )


# In[23]:


result


# In[24]:


from sklearn.preprocessing import StandardScaler
sc = StandardScaler()


# In[25]:


data_scaled = sc.fit_transform(result)


# In[26]:


data_scaled


# In[27]:


from sklearn.cluster import KMeans


# In[28]:


model = KMeans(n_clusters=10)


# In[29]:


pred  = model.fit_predict(data_scaled)


# In[30]:


dataset_scaled = pd.DataFrame(data_scaled, columns=['IP', 'Date', 'URL', 'Response Code'])


# In[31]:


dataset_scaled['mycluster'] = pred


# In[32]:


ips = [dataset['Host'], result['IP']]
ips_result = pd.concat(ips, axis=1)


# In[33]:


ips_result


# In[34]:


def CountFrequency(my_list, ip_label): 
  
    # Creating an empty dictionary  
    freq = {} 
    for item in my_list: 
        if (item in freq): 
            freq[item] += 1
        else: 
            freq[item] = 1
    max_freq = 0
    max_key = 0
    for key, value in freq.items(): 
        if value > max_freq:
            max_freq = value
            max_key = key
    
    return ip_label[my_list.index(max_key)]


# In[40]:


res = CountFrequency(ips_result['IP'].tolist(), ips_result['Host'].tolist())


# In[41]:


res = str(res)


# In[42]:


file1 = open("blockIP.txt","w")
file1.write(res)
file1.close()


# In[ ]:




