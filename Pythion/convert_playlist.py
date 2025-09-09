from pytube import Playlist
import webbrowser
import time

# Hlavní funkce
def main():
    # Vstup od uživatele
    PLAYLIST_URL = input("Zadejte URL YouTube playlistu: ").strip()
    
    # Načtení playlistu
    try:
        playlist = Playlist(PLAYLIST_URL)
        print(f"Zpracovávám playlist: {playlist.title}")
        print(f"Počet videí: {len(playlist.video_urls)}")
    except Exception as e:
        print(f"Chyba při načítání playlistu: {e}")
        return
    
    # Procházení videí v playlistu
    for index, video_url in enumerate(playlist.video_urls, 1):
        print(f"Otevírám video {index}/{len(playlist.video_urls)}: {video_url}")
        
        # Vytvoření URL pro ezmp3.to s odkazem na video
        ezmp3_url = f"https://ezmp3.to/?url={video_url}"
        
        # Otevření odkazu v prohlížeči
        try:
            webbrowser.open(ezmp3_url)
            print(f"Otevřeno: {ezmp3_url}")
        except Exception as e:
            print(f"Chyba při otevírání {video_url}: {e}")
        
        # Zpoždění mezi otevíráním odkazů (např. 5 sekund)
        time.sleep(5)  # Upravte podle potřeby
        
    print("Všechny odkazy byly otevřeny v prohlížeči.")

if __name__ == "__main__":
    main()