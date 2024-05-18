#this is a program to learn about pandas
#Contributers:
# Martin Konteh
# Momin Afzal

import pandas as py

#ADD YOUR NAME and AGE TO THE DATA DICTIONARY 

data = {
    'Name': 'Martin',
    'Age': '20',
}

df = py.DataFrame(data, index = [0])
print(df)
