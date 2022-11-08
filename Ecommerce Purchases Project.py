import pandas as pd

# import data
ecom = pd.read_csv('Ecommerce Purchases')

# check data
ecom.head()
ecom.info()

# average purchase price
ecom['Purchase Price'].mean()

# highest and lowest purchase prices
ecom['Purchase Price'].max()
ecom['Purchase Price'].min()

# number of people with English 'en' as their language of choice on the website
ecom[ecom['Language'] == 'en'].count()

# number of people with job title of 'Lawyer'
ecom[ecom['Job']=='Lawyer'].count()

# number of people who made purchases duing the AM and PM
ecom['AM or PM'].value_counts()

# 5 most common job titles
ecom['Job'].value_counts().head(5)

# find purchase price for purchase from Lot: '90 WT'
ecom[ecom['Lot']=='90 WT']['Purchase Price']

# find email of person with a specific credit card number
ecom[ecom['Credit Card'] == 4926535242672853]['Email']

# number of people who have an Amex card and have made a purchase of over $95
ecom[(ecom['CC Provider']=='American Express') & (ecom['Purchase Price']>95)].count()

# number of people who have a credit card that expires in 2025
sum(ecom['CC Exp Date'].apply(lambda expire: expire[3:]=='25'))
# also:
# ecom[ecom['CC Exp Date'].apply(lambda expire: expire[3:]=='25')].count()

# top 5 most popular email providers:
ecom['Email'].apply(lambda email: email.split('@')[1]).value_counts().head(5)