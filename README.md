# Spoti2Yt

Spoti2Yt is a Python project that converts **Spotify playlists into YouTube playlists** by extracting song metadata from Spotify and using it to search and create playlists on YouTube.

The goal of the project is to **simplify cross-platform playlist migration**, allowing users to automatically recreate their Spotify playlists on YouTube.

---

## Project Overview

This project works by:

1. Using the **Spotify API** to read a user's playlist and extract track metadata such as song name and artist.
2. Using the **YouTube Data API** to search for the corresponding videos.
3. Automatically creating a **YouTube playlist**.
4. Adding the matched videos to the created playlist.

This removes the need to manually search and recreate playlists across platforms.

---

## Current Repository State (Recovered)

This repository currently contains a **recovered version of the project script**.

- The **Flask web interface is not included in this version**.
- The original project was designed as a **Flask-based web application**, which will be **re-added later**.
- The script present in this repository **does not work fully in its current state** and is mainly preserved for reference and further development.

Future updates will restore:
- The **Flask backend**
- Proper **API authentication flow**
- A working **end-to-end playlist migration pipeline**

---

## Technologies Used

- Python
- Spotify Web API
- YouTube Data API
- Flask (planned to be restored)

---

## Future Improvements

- Rebuild Flask web interface
- Fix authentication flow
- Improve song matching accuracy
- Add better error handling
- Create a user-friendly interface
