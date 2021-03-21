#!/usr/bin/env python
# coding: utf-8

# # Analyse de données d'Eco2Mix

# In[1]:


# Importations classiques pour le tracé
import pandas as pd
from ipywidgets import interact, interactive, fixed, interact_manual, IntSlider
# Standard plotly imports
import chart_studio.plotly as py
import plotly.graph_objs as go
from plotly.offline import iplot, init_notebook_mode
# Using plotly + cufflinks in offline mode
import cufflinks as cf
cf.go_offline(connected=False)
init_notebook_mode(connected=False)


# In[5]:


df042020=pd.read_csv('data/ELEC01_04_2020.csv')


# In[ ]:




