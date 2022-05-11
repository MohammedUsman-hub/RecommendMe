import numpy as np
import pandas as pd
import sklearn.metrics as metrics
from scipy import sparse
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity





#read_movie = pd.read_sql_table('movie', 'sqlite:///account.db')
#print(read_movie)

#read_event = pd.read_sql_table('event', 'sqlite:///account.db')
#print(read_event)

#read_user = pd.read_sql_table('user', 'sqlite:///account.db')
#print(read_user)

# Collaborative Filtering
#reading csv files
ratings = pd.read_csv('ratings.csv')
movies = pd.read_csv('movies.csv')
ratings = pd.merge(movies, ratings).drop(['genres', 'timestamp'], axis=1)
#print(ratings.shape)
ratings.head()


userRatings = ratings.pivot_table(index=['userId'],columns=['title'],values='rating')
userRatings.head()
#print("Before: ",userRatings.shape)
userRatings = userRatings.dropna(thresh=10, axis=1).fillna(0,axis=1)
#userRatings.fillna(0, inplace=True)
#print("After: ",userRatings.shape)




# building similarity matrix
corrMatrix = userRatings.corr(method='pearson')
corrMatrix.head(100)

def get_similar(movie_name,rating):
    similar_ratings = corrMatrix[movie_name]*(rating-2.5)
    similar_ratings = similar_ratings.sort_values(ascending=False)
    #print(type(similar_ratings))
    return similar_ratings

# User rating drama movies
user_likes_drama = [("Goodfellas (1990)",5),("Casino (1995)",5),("Finding Nemo (2003)",1),("American Pie (1999)",2)]
similar_movies = pd.DataFrame()
for movie,rating in user_likes_drama:
    similar_movies = similar_movies.append(get_similar(movie,rating),ignore_index = True)

print("Drama movie recommendations: ")
#print(similar_movies.head(10))
print(similar_movies.sum().sort_values(ascending=False).head(40))

# User rating comedy movies
user_likes_comedy= [("Big Daddy (1999)",5),("Cool Runnings (1993)",4),("Godfather: Part II, The (1974)",2),("Donnie Brasco (1997)",1)]
similar_movies = pd.DataFrame()
for movie,rating in user_likes_comedy:
    similar_movies = similar_movies.append(get_similar(movie,rating),ignore_index = True)

print()
print("Comedy movie recommendations: ")
#print(similar_movies.head(10))
print(similar_movies.sum().sort_values(ascending=False).head(40))