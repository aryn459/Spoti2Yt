from os import environ
import json
import re
import requests
from urllib.parse import quote

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


SPOTIFY_CLIENT_ID = environ.get("CLIENT_ID")
SPOTIFY_CLIENT_SECRET = environ.get("CLIENT_SECRET")

def get_spotify_tracks(playlist_url):
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET
    ))
    playlist_id = playlist_url.split("/")[-1].split("?")[0]
    results = sp.playlist_tracks(playlist_id)
    tracks = []
    for item in results['items']:
        track = item['track']
        if track:
            name = track['name']
            artist = track['artists'][0]['name']
            tracks.append(f"{name} {artist}")
    return tracks

def scrape_youtube_search(query):
    query_encoded = quote(query)
    url = f"https://www.youtube.com/results?search_query={query_encoded}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                      " Chrome/115.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to get search results for {query}")
        return None

    match = re.search(r'var ytInitialData = ({.*?});</script>', response.text, re.DOTALL)
    if not match:
        print("Could not find ytInitialData in the page.")
        return None

    data = json.loads(match.group(1))

    contents = data['contents']['twoColumnSearchResultsRenderer']['primaryContents']['sectionListRenderer']['contents']

    for section in contents:
        item_section = section.get('itemSectionRenderer', {})
        items = item_section.get('contents', [])
        for item in items:
            video = item.get('videoRenderer')
            if video and 'videoId' in video:
                video_id = video['videoId']
                return f"https://www.youtube.com/watch?v={video_id}"

    print("No video results found in JSON.")
    return None

def main():
    playlist_url = input("Enter Spotify playlist URL: ").strip()
    output_file = input("Enter output filename (e.g. youtube_links.txt): ").strip()

    tracks = get_spotify_tracks(playlist_url)
    print(f"Found {len(tracks)} tracks in Spotify playlist.")

    with open(output_file, "w", encoding="utf-8") as f:
        for track in tracks:
            print(f"Searching YouTube for: {track}")
            link = scrape_youtube_search(track)
            if link:
                print(f"Found: {link}")
                f.write(f"{track} -> {link}\n")
            else:
                print("No video found.")
    print(f"Done! Results saved in {output_file}")

if __name__ == "__main__":
    main()
