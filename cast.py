import bs4
import requests

# Contains methods for getting cast info (from a specifed url)
def get_cast_info(page_url):

    # Try connecting to the URL, throw error if it fails
    try:
        page_source = requests.request('GET', page_url)
        page_source.raise_for_status()
    except requests.exceptions.HTTPError as error:
        print(error)

    # Create initial beautiful soup parse object of the html code for the url
    results_soup = bs4.BeautifulSoup(page_source.text, 'html.parser')
    assert results_soup

    # Store names of cast members
    cast_list = []

    cast_tag_outer = results_soup.find('table', class_='cast_list')
    assert cast_tag_outer

    cast_tag_list = cast_tag_outer.find_all('tr')
    assert cast_tag_list

    # Loop through first 15 tr tags
    count = 0
    for tr in cast_tag_list:
        if count > 15:
            break
        else:
            pass

        # Catch exception for if second td not found -> continue to next iteration
        try:
            second_td = tr.find_all('td')[1]
        except IndexError:
            continue

        assert second_td

        a_tag = second_td.find('a')
        assert a_tag

        name = a_tag.get_text()
        assert name

        # Append to cast_list
        cast_list.append(name)

        count += 1

    return cast_list


def print_cast_members_from_list(cast_list):
    cast_string = ''
    for i in range(len(cast_list)):
        if i == 0:
            # strip() is python functions that removes whitespace/tabs/newline characters
            cast_string += cast_list[i].strip()
        else:
            cast_string += ', ' + cast_list[i].strip()

    return cast_string
