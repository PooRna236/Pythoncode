# -*- coding: utf-8 -*-
"""Untitled20.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pvP6aOgHcd0pKS7J0aP6JhaT_su5IPaZ
"""

data = [{'name':'Chandu','age':23},{'name':'Surya','age':35},{'name':'Venkat','age':45},{'name':'nishant','age':29},{'name':'LeelaKrishna','age':21},{'name':'Durga Prasad','age':24},{'name':'Apparao','age':26},{'name':'RaviTeja','age':26}]

data

def age_values(df):
  for i in df:
    if (i.get('age') > 17 and i.get('age') < 39):
      print(i.get('age'))

age_values(data)

