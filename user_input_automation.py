import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

def get_user_movie_list():
    # INITIAL SETUP
    # Get url of website to visit
    url = "https://imdb.com"

    # Option to run with headless browser
    option = webdriver.ChromeOptions()
    option.add_argument('headless')

    # Visiting requested url defined above
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
    driver.get(url)

    # Starting the lists that will be used to generate user's list of movie ids and names
    user_movie_list_names = []
    user_movie_list_ids = []

    print('Type "Stop" to finalize your list!')
    while True:
        # Finding the search bar from requested url
        search_bar = driver.find_element(By.ID, 'suggestion-search')
        assert search_bar

        # Allowing user input to populate search bar
        search_bar.clear()
        user_input = input('What movie to search? ')

        # Allows user to exit loop
        if user_input.lower() == 'stop':
            break

        search_bar.send_keys(user_input)
        search_bar.send_keys(Keys.RETURN)
        assert 'No results found.' not in driver.page_source

        element = driver.find_element(By.XPATH, "/html[1]/body[1]/div[3]/div[1]/div[2]/div[3]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[1]/a[1]/img[1]")
        element.click()

        movie_list_names = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/h1').text
        user_movie_list_names.append(movie_list_names)
        print(user_movie_list_names)

        movie_list_ids = driver.find_element(By.XPATH, '/html/head/meta[30]').get_attribute('content')
        user_movie_list_ids.append(movie_list_ids)
        print(user_movie_list_ids)

    driver.quit()
    return user_movie_list_ids
