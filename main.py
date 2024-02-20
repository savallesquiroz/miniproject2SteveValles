#(5/5 points) Initial comments with your name, class and project at the top of your .py file.
# INF601 - Advanced Programming in Python
# Steve Valles Quiroz
# Mini Project 2

#(5/5 points) Proper import of packages used.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#(20/20 points) Using a data source of your choice, such as data from data.gov or using the Faker package, generate or retrieve some data for creating basic statistics on. This will generally come in as json data, etc.
   #"What was world suicide rate in 2023 for males and females?"
   #"How does suicide rates differ from Spain to USA?"
   #"What was world suicide rate change from 2022 to 2023?"
   #"How does suicide rate change differ from male and females?"
   #"How does suicide rate change differ from Spain to USA?"
#(10/10 points) Store this information in Pandas dataframe. These should be 2D data as a dataframe, meaning the data is labeled tabular data.
rates = pd.read_csv('world_suicide_rate_2023.csv', index_col='Country')
#(10/10 points) Using matplotlib, graph this data in a way that will visually represent the data. Really try to build some fancy charts here as it will greatly help you in future homework assignments and in the final project.

#Store world rates from 'World' row
worldRates = rates.loc['World']

#Store suicide rates of 'Male' and 'Female'
maleRates = worldRates['Male']
femaleRates = worldRates['Female']

#Store female and male rates in a numpy array.
maleRateArray = np.array([maleRates])
femaleRateArray = np.array([femaleRates])

#Graph parameters to plot 'Male vs Female Suicide Rate Comparison'
plt.figure(figsize=(10,5)) #Taller and narrower graph as there's only 2 columns
plt.plot(['Male'], maleRateArray, label='Male')# X= 'Male' and Y = 'maleRateArray
plt.plot(['Female'], femaleRateArray, label='Female')# X= 'Female' and Y = femaleRateArray

plt.xlabel('Gender')
plt.ylabel('Suicide Rates')
plt.title('Male vs Female Suicide Rate Comparison')
plt.legend()
#(10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
#Save 'Male vs Female Suicide Rate Comparison' chart.
maleFemaleRates = "charts/maleFemaleRates.png"
plt.savefig(maleFemaleRates)

#(10/10 points) I will be checking out the master branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.
#(20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown. Be thorough on the explanations.