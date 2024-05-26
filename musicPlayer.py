import pygame
import os

def play_music(file_path):
    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the music file
    pygame.mixer.music.load(file_path)

    # Play the music
    pygame.mixer.music.play()

    print(f"Playing {file_path}...")

    # Wait for the music to finish playing
    while pygame.mixer.music.get_busy():
        continue

def main():
    print("Simple Music Player")
    print("===================")

    # Get the path to the music file
    file_path = input("Enter the path to the music file: ")
    
    # Check if the file exists
    if not os.path.exists(file_path):
        print("File not found!")
        return

    # Play the music
    play_music(file_path)

if __name__ == "__main__":
    main()
