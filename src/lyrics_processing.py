import os
import re
from pathlib import Path
from utils import read_config

def clean_lyrics(lyrics):
    cleaned_lyrics = re.sub(r'\[.*?\]', '', lyrics)
    cleaned_lyrics = re.sub(r'[^a-zA-Z\s]', '', cleaned_lyrics)
    cleaned_lyrics = cleaned_lyrics.lower()
    cleaned_lyrics = re.sub(r'\s+', ' ', cleaned_lyrics).strip()
    return cleaned_lyrics

def preprocess_lyrics(input_dir, output_dir):
    for song_file in input_dir.glob("*.txt"):
        with open(song_file, 'r', encoding='utf-8') as f:
            lyrics = f.read()

        cleaned_lyrics = clean_lyrics(lyrics)

        cleaned_file = output_dir / song_file.name
        with open(cleaned_file, 'w', encoding='utf-8') as f:
            f.write(cleaned_lyrics)

if __name__ == "__main__":
    ###################
    ### Read Config ###
    ###################
    config = read_config()
    raw_lyrics_dir = Path(config['lyrics_path']['raw_inputs'])
    cleaned_lyrics_dir = Path(config['lyrics_path']['cleaned_inputs'])

    ###############################
    ### Create Output directory ###
    ###############################
    cleaned_lyrics_dir.mkdir(parents=True, exist_ok=True)

    #################################
    ### Clean up each lyrics file ###
    #################################
    preprocess_lyrics(raw_lyrics_dir, cleaned_lyrics_dir)
