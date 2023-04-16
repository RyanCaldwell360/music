import os
import csv
import torch
import pandas as pd
from pathlib import Path
from transformers import DistilBertTokenizer, DistilBertModel
from utils import extract_embeddings, read_config, read_lyrics_from_files

def extract_artist_song_lyrics(path):
    artists = []
    songs = []
    lyrics = []
    lyrics_dir = Path(path)

    for file in lyrics_dir.glob("*.txt"):
        file_name = file.name.split('-')
        artist = file_name[0]
        song = file_name[1][:-4] # ignoring .txt

        artists.append(artist)
        songs.append(song)

        with open(file, "r", encoding="utf-8") as f:
            lyrics.append(f.read())

    return artists, songs, lyrics

if __name__ == "__main__":
    ######################################
    ### Load tokenizer and transformer ###
    ######################################
    tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
    model = DistilBertModel.from_pretrained('distilbert-base-uncased')

    ###################
    ### Read Config ###
    ###################
    config = read_config()
    cleaned_lyrics_dir = Path(config['lyrics_path']['cleaned_inputs'])
    output_path = Path(config['lyrics_path']['embeddings'])

    output_path.mkdir(parents=True, exist_ok=True)

    #####################
    ### Read in Songs ###
    #####################
    artists, songs, lyrics = extract_artist_song_lyrics(cleaned_lyrics_dir)

    ###################
    ### Embed songs ###
    ###################
    embeddings = extract_embeddings(lyrics, model, tokenizer)
    embeddings = pd.DataFrame(embeddings)

    ###########################
    ### Write Embeds to CSV ###
    ###########################
    output = pd.DataFrame({'artists':artists,
                           'songs':songs})
    output = pd.concat([output, embeddings], axis=1)
    output.to_csv(output_path / 'embeddings.csv', header=True, index=False)
