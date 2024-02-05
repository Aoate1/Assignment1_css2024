# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 14:04:40 2024

@author: Aoate Tsimatsima
"""

#Movie assignment
import pandas as pd
df_movies_all = pd.read_csv("movie_dataset.csv")

df_movies
df_movies.info()
df_movies.describe()
df_movies.columns.tolist()
df_movies.columns = df_movies.columns.str.replace(' ', '_') 
df_movies.columns = df_movies.columns.str.replace('(', '') 
df_movies.columns = df_movies.columns.str.replace(')', '') 
df_movies.columns.tolist()


df_movies.dropna(inplace = True)
df_movies = df_movies.reset_index(drop=True)
df_movies.drop_duplicates(inplace = True)
print(df_movies)


#Question1
Rating = df_movies.sort_values('Rating')
#data shown from lowest to highest just by the rating column

#Question 2
mean_revenue = df_movies["Revenue_Millions"].mean()
print(mean_revenue)
#the mean was calculated and a variable was made

#Question 3

Year_sort = df_movies.sort_values('Year')

Year_2015_up = Year_sort[Year_sort['Year'] > 2014]
mean_revenue_2015 = Year_2015_up["Revenue_Millions"].mean()
#since the last year of my dataframe is 2016 the average will be calculated from 2015 to 2016

year = df_movies.sort_values('Year')

print(mean_revenue_2015)

#Question 4
#Since my previous transformation removed a few of the movies I used the old dataframe and filtered out all the years before 2016
df_movies_all = pd.read_csv("movie_dataset.csv")


df_movies_all


Year_2016_all = df_movies_all[df_movies_all['Year'] > 2015]

#Question 5
#Using the filtering option, I put his movies in one variable
#I had to use the dataframe with all the data before removing the row that were empty
df_movies_all[df_movies_all['Director']] == 'Christopher Nolan'
Chris_Nolan = df_movies_all[df_movies_all['Director'] == 'Christopher Nolan']
print(Chris_Nolan)

# Qiestion 6

Rating_over8 = df_movies_all[df_movies_all['Rating'] >= 8]
Rating_over8

#Question 7

mean_revenue = df_movies["Revenue_Millions"].mean()

Chris_Nolan_median = Chris_Nolan["Rating"].median()
Chris_Nolan_median

#Question 8
#Create a data set for each year
df_movies_all_year_sort = df_movies_all.sort_values('Year')
Year_2016 = df_movies_all[df_movies_all['Year'] == 2016]
Year_2008 = df_movies_all[df_movies_all['Year'] == 2008]
Year_2007 = df_movies_all[df_movies_all['Year'] == 2007]
Year_2006 = df_movies_all[df_movies_all['Year'] == 2006]

#Calculate the average for each years dataset
Rating_2016 = Year_2016["Rating"].mean()
Rating_2008 = Year_2008["Rating"].mean()
Rating_2007 = Year_2007["Rating"].mean()
Rating_2006 = Year_2006["Rating"].mean()
#then check from variable explorer or print
#Or the below code can be used 
df_movies_all.groupby("Year").agg({"Rating":"mean"}) 

#Question 9


movies_2006 = df_movies_all[df_movies_all['Year'] == 2006].shape[0]
movies_2016 = df_movies_all[df_movies_all['Year'] == 2016].shape[0]
# Calculate the percentage increase
percentage_increase = ((movies_2016 - movies_2006) / movies_2006) * 100
print(percentage_increase)

#Question 10

#We can target the mentioned names and see which ones from the list have the highest frequency
Actor_name = 'Chris Pratt'
name_frequency = df_movies_all['Actors'].str.count(Actor_name).sum()
print(name_frequency)

Actor_name = 'Bradley Cooper'
name_frequency = df_movies_all['Actors'].str.count(Actor_name).sum()
print(name_frequency)

Actor_name = 'Mark Wahlberg'
name_frequency = df_movies_all['Actors'].str.count(Actor_name).sum()
print(name_frequency) #Highest occurences of this actors name

Actor_name = 'Matthew McConaughey'
name_frequency = df_movies_all['Actors'].str.count(Actor_name).sum()
print(name_frequency)


#Question 11
#The first this to do is create a dataframe for the string data contained in the Genre column
# This can be followed by using nunique to count the number of unique genres
df_genres = df_movies_all['Genre'].str.split(',').explode().str.strip()
genres_count_unique = df_genres.nunique()   
print(genres_count_unique)

#Question 12

import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sb

correlation = df_movies_all['Runtime (Minutes)'].corr(df_movies_all['Rating'])
sb.lineplot(x='Runtime (Minutes)', y='Rating', data=df_movies_all)
plt.title(f'Correlation between Runtime and Rating in of movies: {correlation:.2f}')
plt.show()
#There was a dip in ratings when the runtime was shorter 
#From the graph, it can be seen that there seems to be a steady increase in ratings as the runtime increases
#I would advice the directors to work aroud a run time of approximately 150 minutes for better ratings
correlation = df_movies_all['Runtime (Minutes)'].corr(df_movies_all['Rank'])
sb.lineplot(x='Runtime (Minutes)', y='Rank', data=df_movies_all)
plt.title(f'Correlation between Runtime and Rank in of movies: {correlation:.2f}')
plt.show()
# The graph shows inconsistencies between the rank and runtime 
#We can conclude that the run time does not affect the ranking of the movies
#The directors should keep the run time around 150 minutes due to the witnessed peak in ranking

#correlation = df_movies_all['Rank'].corr(df_movies_all['Runtime (Minutes)'])# check graph
#sb.scatterplot(x='Rank', y='Runtime (Minutes)', data=df_movies_all) #dont forget to remove


correlation = df_movies['Year'].corr(df_movies['Revenue_Millions)'])
sb.lineplot(x='Year', y='Revenue_Millions)', data=df_movies)
#Note the dataframe used is one with no NAN cells therefore the dataframe has reduced rows
#seems to be a decline in revenue with increasing years with 2009 being the peak revenue year of the recored years
#The directors should be aware of the decrease in revenue, this trend seems to be mindful of the budget cost for the movies

correlation = df_movies_all['Year'].corr(df_movies_all['Votes'])
sb.lineplot(x='Year', y='Votes', data=df_movies_all)
#from 2006 to 2016, there is a notable decline in the number of votes for the movies
#2016 has the lowest number of votes while the peak number of votes was seen in 2012
#The director should create an interactive platform that can increase votes which could affect the metascore because it is also a ranking based on critics

correlation = df_movies['Metascore'].corr(df_movies['Revenue_Millions)'])
sb.scatterplot(x='Metascore', y='Revenue_Millions)', data=df_movies)
#There seems to be a generally normal distribution between the metascore and its correlation to the revenue
#This means that generally most movies with average metascore will yield average revenues
#The outliers also indicates that that a good movie that generates a relatively high metascore can gererate high revenue












df_movies.columns
df_movies_all.plot(x = "Year", y = ["Rating", "Runtime (Minutes)"])





