#(5/5 points) Initial comments with your name, class and project at the top of your .py file.
# INF601 - Advanced Programming in Python
# Steve Valles Quiroz
# Mini Project 2

#(5/5 points) Proper import of packages used.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

#Create 'charts' folder.
try:
    Path("charts").mkdir()
except FileExistsError:
    pass
#(20/20 points) Using a data source of your choice, such as data from data.gov or using the Faker package, generate or retrieve some data for creating basic statistics on. This will generally come in as json data, etc.
   #"1.What was world suicide rate in 2023 for males and females?"
   #"2.Which were top 5 countries with lower suicide rates?"
   #"3.Which were top 5 countries with higher suicide rates?"
   #"4.Which were top 5 countries with lowest change%?"
   #"5.Which were top 5 countries with highest change%?"

#(10/10 points) Store this information in Pandas dataframe. These should be 2D data as a dataframe, meaning the data is labeled tabular data.
rates = pd.read_csv('world_suicide_rate_2023.csv', index_col='Country')
data = pd.read_csv('world_suicide_rate_2023.csv')
#(10/10 points) Using matplotlib, graph this data in a way that will visually represent the data. Really try to build some fancy charts here as it will greatly help you in future homework assignments and in the final project.

#1. Store world rates from 'World' row
worldRates = rates.loc['World']
# Store suicide rates of 'Male' and 'Female'
maleRates = worldRates['Male']
femaleRates = worldRates['Female']
# Store female and male rates in a numpy array.
maleRateArray = np.array([maleRates])
femaleRateArray = np.array([femaleRates])

#2. Store sorted data by top 5 lowest suicide rates
lowRateTop5 = data.nsmallest(5, 'All')

#3. Store sorted data by top 5 higher suicide rates
highRateTop5 = data.nlargest(5, 'All')

#4. Store sorted data by top 5 lowest suicide change%
lowChangeTop5 = data.nsmallest(5, 'Change%')

#5. Store sorted data by top 5 highest suicide change%
highChangeTop5 = data.nlargest(5, 'Change%')

#1. Graph parameters to plot 'Male vs Female Suicide Rate Comparison'
plt.figure(figsize=(5,8)) #Taller and narrower graph as there's only 2 columns
plt.bar(['Male'], maleRateArray, label='Male') # X= 'Male' and Y = 'maleRateArray
plt.bar(['Female'], femaleRateArray, label='Female') # X= 'Female' and Y = 'femaleRateArray'

plt.xlabel('Gender')
plt.ylabel('Suicide Rates')
plt.title('Male vs Female Suicide Rate Comparison')
plt.legend()
#1. Save graph
maleFemaleRate = "charts/maleFemaleRate.png"
plt.savefig(maleFemaleRate)
plt.show()

#2. Graph parameters to plot 'top 5 countries with lowest suicide rates'
plt.figure(figsize=(12,5))
plt.bar(lowRateTop5['Country'], lowRateTop5['All']) #X and Y

plt.xlabel('Country')
plt.ylabel('Suicide Rate')
plt.title('Top 5 Countries with Lower Suicide Rates')
#2. Save graph
lowRateTop5Chart = "charts/lowRateTop5.png"
plt.savefig(lowRateTop5Chart)
plt.show()

#3. Graph parameters to plot 'top 5 countries with highest suicide rates'
plt.figure(figsize=(10,5))
plt.bar(highRateTop5['Country'], highRateTop5['All']) #X and Y

plt.xlabel('Country')
plt.ylabel('Suicide Rate')
plt.title('Top 5 Countries with Highest Suicide Rates')
#3. Save graph
highRateTop5Chart = "charts/highRateTop5.png"
plt.savefig(highRateTop5Chart)
plt.show()

#4. Graph parameters to plot 'top 5 countries with lowest suicide change%'
plt.figure(figsize=(14,5))
plt.bar(lowChangeTop5['Country'], lowChangeTop5['Change%']) #X and Y

plt.xlabel('Country')
plt.ylabel('Suicide Change')
plt.title('Top 5 Countries with Suicide Decreasing')
#4. Save graph
bestChangeTop5Chart = "charts/bestChangeTop5.png"
plt.savefig(bestChangeTop5Chart)
plt.show()

#5. Graph parameters to plot 'top 5 countries with highest suicide change%'
plt.figure(figsize=(10,5))
plt.bar(highChangeTop5['Country'], highChangeTop5['Change%']) #X and Y

plt.xlabel('Country')
plt.ylabel('Suicide Change')
plt.title('Top 5 Countries with Suicide Increasing')
#5. Save graph
worseChangeTop5Chart = "charts/worseChangeTop5.png"
plt.savefig(worseChangeTop5Chart)
plt.show()

#(10/10 points)Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.


#(10/10 points) I will be checking out the master branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.
#(20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown. Be thorough on the explanations.