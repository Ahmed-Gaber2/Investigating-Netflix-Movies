#use python to have answer if the netflix have shorter movies
#data using is provided from netflix statics

# data given by kaggle and neat it by datacamp
# create list to entre the data and from it begin structure to have dataframe
years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93,90]
movie_dict = {"years": years,"durations": durations}
print(movie_dict)                       #Test the data on the dictionary

import pandas as pd                     #import panda library as alies pd  
durations_pf= pd.DataFrame(movie_dict)  # Create a DataFrame from the dictionary
print(durations_pf)                     #Test the DataFrame

import matplotlib.pyplot as plt         #Import matplotlib.pyplot under the alias plt
plt.plot(years, durations)              #Line plot (X-axis= years, Y-axis= durations)
plt.title("Netflix Movie Durations 2011-2020") #Add title for the graph
plt.show()                              #The have a graph for the data

#import file CSV of Netflix_data
netflix_df= pd.read_csv("E:\Data scientists\Project Investigating Netflix Movies and Guest Stars in The Office (project 1)\\netflix_data.csv")
#print(netflix_df.iloc[:5]) #print only five lines of the CSV file 
print(netflix_df.head())    #another way for print only five lines of the CSV file

#Subset the netflix_df DataFrame such that only rows where the type is a "Movie"
netflix_df_movies_only= netflix_df[netflix_df['type'] == 'Movie'] # Filter the Dataframe
#DataFrame to preserve only the columns title, country, genre, release_year, and duration
netflix_movies_col_subset= netflix_df_movies_only[['title','country','genre','release_year','duration']] 
print(netflix_movies_col_subset[0:10]) #Print the first five rows of

# Using netflix_movies_col_subset DataFrame, create a scatter plot 
fig = plt.figure(figsize=(10,25)) # Create a figure and increase the figure size
plt.scatter(netflix_movies_col_subset['release_year'],netflix_movies_col_subset['duration']) # Create a scatter plot of duration versus year
plt.title("Movie Duration by Year of Release") # Create a title
plt.show()                                     #plt show

# Filter for durations shorter than 60 minutes
short_movies = netflix_movies_col_subset[netflix_movies_col_subset['duration'] < 60] 
print(short_movies[:20])      # Print the first 20 rows of short_movies

colors = [] # Define an empty list
# Iterate over rows of netflix_movies_col_subset
for lab , row  in netflix_movies_col_subset.iterrows():
    if row["genre"] == "children" :
        colors.append("red")
    elif row["genre"] == "Documentaries" :
        colors.append("blue")
    elif row["genre"] == "Stand-Up" :
        colors.append("green") 
    else:
        colors.append("black")        
print(colors[:10]) # Inspect the first 10 values in your list

# Using netflix_movies_col_subset DataFrame, create a scatter plot 
plt.style.use('fivethirtyeight')
fig = plt.figure(figsize=(10,25)) # Create a figure and increase the figure size
# Create a scatter plot of duration versus release_year
plt.scatter(netflix_movies_col_subset['release_year'],netflix_movies_col_subset['duration'],c=colors)
# Create a title and axis labels
plt.title("Movie Duration by Year of Release") 
plt.xlabel("Release year")
plt.ylabel("Duration (min)")
plt.show()                                     #plt show
are_movies_getting_shorter = "maybe"
