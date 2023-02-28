#!/usr/bin/env python
# coding: utf-8

# In[3]:


f=open("skill.txt","x")
f.close()


# In[4]:


f=open("skill.txt","x")
f.close()


# In[7]:


f=open("skill.txt","r")
print(f.read(12))
f.close()


# In[8]:


f=open("data.txt","a")
f.write("\nthis is for append function")
f.close()


# In[11]:


f=open("skill.txt","r")
f.seek(0)
print(f.readlines())
f.close()


# In[12]:


f=open("data.txt","w")
string="FITA acadamy in Tnagar"
loc=["chennai\n","kochin\n","delhi"]
f.write(string)
f.writelines(loc)
f.close()


# In[13]:


f=open("data.txt","w+")
print(f.read())
f.close()


# In[ ]:




