import csv
import torch
import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.neighbors import NearestNeighbors
from utils import extract_embeddings, read_config
from transformers import DistilBertTokenizer, DistilBertModel

def read_embeddings(file_path):
    data = pd.read_csv(file_path)

    return data

def find_similar_songs(prompt_embeds, song_embeds, top_k):
    knn = NearestNeighbors(n_neighbors=top_k, metric='cosine')
    knn.fit(song_embeds)
    _, indices = knn.kneighbors(prompt_embeds)

    indices = indices[0]
    return indices

if __name__ == "__main__":
    ###################
    ### Read Config ###
    ###################
    config = read_config()
    embeddings_path = Path(config['lyrics_path']['embeddings'])
    embeddings_file = embeddings_path / 'embeddings.csv'

    ######################################
    ### Read tokenizer and transformer ###
    ######################################
    tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
    model = DistilBertModel.from_pretrained('distilbert-base-uncased')

    ############################
    ### Read Song Embeddings ###
    ############################
    songs_df = read_embeddings(embeddings_file)
    artists = songs_df['artists']
    songs = songs_df['songs']
    song_embeds = songs_df.drop(['artists','songs'], axis=1)\
                          .values

    ################################
    ### Create Prompt Embeddings ###
    ################################
    prompt = config['prompt']
    prompt_embeds = np.array(extract_embeddings(prompt, model, tokenizer)).reshape(1, -1)

    ###########################
    ### kNN for top k songs ###
    ###########################
    similar_song_indexes = find_similar_songs(prompt_embeds, song_embeds, top_k=config['kNN'])
    return_artist_list = artists[similar_song_indexes]
    return_song_list = songs[similar_song_indexes]
    zipped = zip(return_artist_list, return_song_list)

    print("Top X similar songs:")
    for rank, (artist, song) in enumerate(zipped):
        print(f"{rank}. {artist} - {song}")
