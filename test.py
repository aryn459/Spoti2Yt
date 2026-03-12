import datetime
import requests
from bs4 import BeautifulSoup
from os import environ
import spotipy
from spotipy.oauth2 import SpotifyOAuth


# spotify_client = environ.get("SPOTIPY_CLIENT_ID")
# spotify_secret = environ.get("SPOTIPY_CLIENT_SECRET")
# spotify_redirect = environ.get("SPOTIPY_REDIRECT_URI")
#
# url = "https://www.billboard.com/charts/hot-100/"
# date = input("Which year would you like to travel to? In YYYY-MM-DD/ Today: ")
#
# if date.title() == "Today":
#     date = datetime.date.today()
#
#
# final_url = url +f"{date}/"
#
#
# response = requests.get(url=final_url)
# response.raise_for_status()
#
# soup = BeautifulSoup(response.text, "html.parser")
# songs = soup.find_all(name="div", class_ = "o-chart-results-list-row-container")
# song_names = [part.find(name="h3", id = "title-of-a-story").string.strip() for part in songs]
#

scope = "playlist-modify-private"
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(client_id= "e57f293adf0d4947b3d38aa18b3bb6b1", client_secret= "f0858988fee04341b6e6701bbac33ddb", redirect_uri="https://open.spotify.com", scope=scope
    )
)

