import yaml
import torch
from pathlib import Path

def read_config(config_file="./src/config.yaml"):
    with open(config_file, "r") as file:
        config = yaml.safe_load(file)
    return config

def read_lyrics_from_files(path):
    lyrics = []
    lyrics_dir = Path(path)

    for file in lyrics_dir.glob("*.txt"):
        with open(file, "r", encoding="utf-8") as f:
            lyrics.append(f.read())

    return lyrics

def extract_embeddings(text, model, tokenizer):
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).squeeze().tolist()