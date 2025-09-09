from pytube import Playlist

# Zadej URL playlistu
playlist_url = 'https://youtube.com/playlist?list=PLbrOLuZ6ec5HMO6HT0jejXKmY6uHXq_3L&si=34J6z5CxU_C3nEui'

# Vytvoření playlist objektu
playlist = Playlist(playlist_url)

# Otevření textového souboru pro zápis
with open('video_links.txt', 'w') as file:
    # Projdeme všechny videa v playlistu
    for video in playlist.videos:
        # Získáme URL videa a zapíšeme do souboru
        file.write(video.watch_url + '\n')

print('Odkazy na videa byly uloženy do souboru video_links.txt')
