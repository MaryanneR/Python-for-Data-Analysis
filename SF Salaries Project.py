import pandas as pd

# import Salaries data
sal = pd.read_csv('Salaries.csv')

# Check data
sal.head()
sal.info()

# Find average Base Pay
sal['BasePay'].mean()

# highest amount of Overtime Pay
sal['OvertimePay'].max()

# find job title of entry JOSEPH DRISCOLL
sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['JobTitle']

# find JOSEPH DRISCOLL's total pay + benefits
sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['TotalPayBenefits']

# highest paid person (total pay + benefits)
sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]

# can also use:
# sal.loc[sal['TotalPayBenefits'].idxmax()]

# lowest paid person (total pay + benefits)
sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].min()]

# average base pay of all employees per year
sal.groupby('Year').mean()['BasePay']

# number of unique job titles
sal['JobTitle'].nunique()

# five most common jobs
sal['JobTitle'].value_counts().head(5)

# job titles represented by one person in 2013
sum(sal[sal['Year']==2013]['JobTitle'].value_counts() == 1)

# number of people with word 'Chief' in their job title
potentialChiefs = sal['JobTitle'].tolist()
realChiefs = list(filter(lambda x: 'chief' in x.lower(),potentialChiefs))
len(realChiefs)

# potential correlation between length of the job title string and salary
sal['title_len'] = sal['JobTitle'].apply(len)
sal[['TotalPayBenefits','title_len']].corr()
# no correlation found