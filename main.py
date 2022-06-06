import bs4
import requests
from imdb_scraper import get_movie_metadata
from user_input_automation import get_user_movie_list

#TODO: Figure out selenium and parse first result of imdb from user input
# Get more in depth information on the movie. ie; cast members, imdb rating, popularity, etc
# Figure out request library for top cast
# Convert data to csv
# Visualize data in tableau

get_movie_metadata(get_user_movie_list())




