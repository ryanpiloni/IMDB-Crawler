import bs4
import requests
from imdb_scraper import get_movie_metadata

#TODO: Figure out selenium and parse first result of imdb from user input
# Get more in depth information on the movie. ie; cast members, imdb rating, popularity, etc
# Figure out request library for top cast
# Convert data to csv
# Visualize data in tableau

movie_ids = ['tt0361748', 'tt0145487', 'tt0325980', 'tt1520211', 'tt4383594']

get_movie_metadata(movie_ids)




