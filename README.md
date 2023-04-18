# music

## About the Project

This repository is a comprehensive solution for analyzing and finding similar songs from the music artist NF based on the user's emotions or thoughts. The project consists of multiple components that work together to fetch the lyrics of NF's songs, preprocess and clean the lyrics, generate embeddings for each song, and finally, search for the most similar songs based on the user's input. The goal of this project is to provide a seamless and interactive way for users to discover and connect with NF's music on a deeper level, helping them find the songs that resonate most with their current emotional state or thoughts. By leveraging state-of-the-art NLP techniques and efficient algorithms, this repository aims to enhance users' music exploration experience, making it more personal and engaging.

## File Structure

```
music
├── src
│   ├── config.yaml
│   ├── utils.py
│   ├── embeddings.py
│   ├── fetch_lyrics.py
│   ├── lyrics_preprocessing.py
│   └── similarity_search.py
└── data
    ├── embeddings
    │   └── .gitkeep
    └── lyrics
        ├── raw_lyrics
        │   └── .gitkeep
        └── cleaned_lyrics
            └── .gitkeep
├── .gitignore
├── README.md
├── requirements.txt
└── run.py
```

## Getting Started

Follow these instructions to set up and run this project on your local machine.

### 1. Setup Genius Account

- Visit the [Genius website](https://genius.com/) and sign up for an account if you don't have one already.

### 2. Create Genius API Client

- Go to the API Clients [page](https://genius.com/api-clients) and sign in with your Genius account.
- Click on "New API Client" and fill in the required information to create a new API client.

### 3. Generate Genius API Access Token

- After creating the API client, click on the "Generate Access Token" button to generate a new access token.

### 4. Set Environment Variable with Access Token

- Save the access token as an environment variable on your local machine. Can do so searching Windows with "System Properties --> Advanced --> Environment Variables --> System Variables".

### 5. Tailor Config
- Open the config.yaml file located in the src directory.
- Update the artists list with the names of the artists whose songs you want to analyze.
- Save the changes to the config.yaml file.

### 6. Execute Pipeline
- Open a terminal or command prompt, navigate to the root directory of the project, and run the following command:

```python
python run.py
```

This will execute the requirements.txt file to install all necessary packages and then begin executing the entire pipeline.
