from itertools import count
from urllib import response
from bs4 import BeautifulSoup as SOUP
import re
from matplotlib.pyplot import title
import requests as HTTP


def main(emotion):

    if emotion == "Sad":
        urlhere = "http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter, asc"

    elif emotion == "Happy":
        urlhere = "http://www.imdb.com/search/title?genres=comedy&title_type=feature&sort=moviemeter, asc"

    elif emotion == "Angry":
        urlhere = "http://www.imdb.com/search/title?genres=action&title_type=feature&sort=moviemeter, asc"

    elif emotion == "Fearful":
        urlhere = "http://www.imdb.com/search/title?genres=fantasy&title_type=feature&sort=moviemeter, asc"

    elif emotion == "Disgust":
        urlhere = "http://www.imdb.com/search/title?genres=fantasy&title_type=feature&sort=moviemeter, asc"

    if emotion == "Trust":
        urlhere = "http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter, asc"

    elif emotion == "Happy":
        urlhere = "http://www.imdb.com/search/title?genres=comedy&title_type=feature&sort=moviemeter, asc"

    elif emotion == "Surprise":
        urlhere = "http://www.imdb.com/search/title?genres=action&title_type=feature&sort=moviemeter, asc"

    elif emotion == "Enjoyment":
        urlhere = "http://www.imdb.com/search/title?genres=fantasy&title_type=feature&sort=moviemeter, asc"

    elif emotion == "Anticipation":
        urlhere = "http://www.imdb.com/search/title?genres=fantasy&title_type=feature&sort=moviemeter, asc"

        response = HTTP.get(urlhere)
        data = response.text

        soup = SOUP(data, "html.parser")

        title = soup.find_all("a", attrs={"href": re.compile("/title/tt+\d+")})
        return title

    if __name__ == "__main__":

        emotion = input("Enter the emotion: ")
        a = main(emotion)
        count = 0

    if (
        emotion == "Disgust"
        or emotion == "Fearful"
        or emotion == "Angry"
        or emotion == "Sad"
        or emotion == "Trust"
        or emotion == "Happy"
        or emotion == "Surprise"
        or emotion == "Enjoyment"
        or emotion == "Anticipation"
    ):
        for i in a:

            # Splitting each line of the
            # IMDb data to scrape movies
            tmp = str(i).split(">;")

            if len(tmp) == 3:
                print(tmp[1][:-3])

            if count > 13:
                break
            count += 1
    else:
        for i in a:
            tmp = str(i).split(">")

            if len(tmp) == 3:
                print(tmp[1][:-3])

            if count > 11:
                break
            count += 1
