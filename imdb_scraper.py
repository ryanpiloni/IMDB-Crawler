import bs4
import requests

from cast import get_cast_info, print_cast_members_from_list

def get_movie_metadata(movie_id_list):
    for id in movie_id_list:

        page_url = 'https://www.imdb.com/title/' + id + '/'

        # Try connecting to the URL, throw error if it fails
        try:
            page_source = requests.request('GET', page_url)
            page_source.raise_for_status()
        except requests.exceptions.HTTPError as error:
            print(error)

        # Create initial beautiful soup parse object of the html code for the url
        results_soup = bs4.BeautifulSoup(page_source.text, 'html.parser')
        assert results_soup

        # Start finding different html tags
        title = results_soup.find('h1', class_='sc-b73cd867-0')
        assert title

        director = results_soup.find('a', class_='ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link')
        assert director

        year = results_soup.find('a', class_='ipc-link ipc-link--baseAlt ipc-link--inherit-color sc-8c396aa2-1 WIUyh')
        assert year

        # This gets us further into the html parse, near the tag with the rating text
        mpa_rating_outer_tag = results_soup.find('div', class_='sc-94726ce4-3 eSKKHi') #This class data changes, is there anyway to avoid having to rely on this? v.v
        assert mpa_rating_outer_tag

        # Returns list containing all a tags (within reach)
        mpa_rating = mpa_rating_outer_tag.find_all('a')
        assert mpa_rating
        mpa_rating_text = mpa_rating[1].get_text()

        # Get movie length (use mpa_rating_outer_tag as start point)
        li_list = mpa_rating_outer_tag.find_all('li')
        assert li_list
        
        movie_length = li_list[2].get_text()
        assert movie_length

        # If length isn't a number, set it to null
        if not movie_length[0].isdigit():
            movie_length = "NULL"
        else:
            pass

        imdb_rating = results_soup.find('span', class_='sc-7ab21ed2-1 jGRxWM')
        assert imdb_rating

        popularity = results_soup.find('div', class_='sc-edc76a2-1 gopMqI')
        if popularity is None:
            popularity_text = 'NULL'
        else:
            popularity_text = popularity.get_text()

        # At this point, get link for top cast...
        cast_list_link = 'https://www.imdb.com/title/' + id + '/fullcredits'

        # List of cast names
        cast_list = get_cast_info(cast_list_link)


        print("---------")
        print("ID: " + id)
        print('URL: ' + page_url)
        print('Movie: ' + title.get_text())
        print('Director: ' + director.get_text())
        print('Year: ' + year.get_text())
        print('Rating: ' + mpa_rating_text)
        print('Length: ' + movie_length)
        print('IMDB Rating: ' + imdb_rating.get_text())
        print('Popularity: ' + popularity_text)
        print('Cast Members: ' + print_cast_members_from_list(cast_list))

    return