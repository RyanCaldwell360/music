import os
import yaml
from pathlib import Path
from lyricsgenius import Genius
from utils import read_config, read_lyrics_from_files

###############################
### Define Helper Functions ###
###############################

def save_lyrics_to_file(artist, title, lyrics, path):
    filename = f"{artist} - {title}.txt"
    lyrics_dir = Path(path)
    lyrics_dir.mkdir(parents=True, exist_ok=True)

    with open(lyrics_dir / filename, "w", encoding="utf-8") as file:
        file.write(lyrics)

def fetch_lyrics_for_artist(artist_name, api_key, path):
    genius = Genius(api_key)
    artist = genius.search_artist(artist_name, max_songs=5, sort="popularity", include_features=False)

    for song in artist.songs:
        song_title = song.title
        song_lyrics = song.lyrics
        save_lyrics_to_file(artist_name, song_title, song_lyrics, path)

if __name__ == "__main__":
    ###########################
    ### Read in Config file ###
    ###########################
    config = read_config()
    print(config)
    artists = config['artists']
    lyrics_path = config['lyrics_path']['raw_inputs']
    API_KEY = os.environ["GENIUS_API_KEY"]

    #######################################
    ### Extract Lyrics for each artisti ###
    #######################################
    for artist in artists:
        print(f"Fetching lyrics for {artist}...")
        fetch_lyrics_for_artist(artist, API_KEY, lyrics_path)
        print(f"Lyrics for {artist} fetched successfully.")

    ############################
    ### Show Number of Songs ###
    ############################
    all_lyrics = read_lyrics_from_files(lyrics_path)
    print(f"Read {len(all_lyrics)} lyrics from files.")
