import pygame

def play_wave(file_name):
    # Initialize Pygame
    pygame.init()
    file_path = "C:\\Users\\gotze\\OneDrive\\Desktop\\ESD\\"+file_name

    try:
        # Load the MP3 file
        pygame.mixer.music.load(file_path)

        # Play the MP3 file
        pygame.mixer.music.play()

        # Wait for the music to finish playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Cleanup
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        pygame.quit()


#def play_wave(file_name):
#    file_path = "C:\\Users\\gotze\\OneDrive\\Desktop\\ESD\\"+file_name
#    pygame.mixer.init()
#    try:#
#        pygame.mixer.music.load(file_path)
#        pygame.mixer.music.play()
 #   except pygame.error as e:
 #       print(f"Error loading or playing sound file: {e}")


# Example usage
#mp3_file_path = "C:\\Users\\gotze\\OneDrive\\Desktop\\ESD\\myrecording140.wav"
