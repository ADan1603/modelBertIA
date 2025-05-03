#!/usr/bin/env python
# coding: utf-8

# In[4]:


from fastapi import FastAPI
import uvicorn


# In[5]:


app = FastAPI()

@app.get("/")
def root():
    return {"mensaje": "Hola desde archivo .py"}


# In[ ]:




