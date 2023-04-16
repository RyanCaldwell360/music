import os
import subprocess

def install_requirements():
    print("Installing requirements...")
    result = subprocess.run(["pip", "install", "-r", "requirements.txt"])
    if result.returncode != 0:
        print("Error installing requirements. Please check the error message above.")
        exit(1)
    print("Requirements installed successfully.")

def main():
    print("Running the lyrics fetching script...")
    os.system("python src/fetch_lyrics.py")

    print("Running the lyrics processing script...")
    os.system("python src/lyrics_processing.py")

    print("Running the embeddings script...")
    os.system("python src/embeddings.py")

    print("Running the similarity search script...")
    os.system("python src/similarity_search.py")

if __name__ == "__main__":
    install_requirements()
    main()