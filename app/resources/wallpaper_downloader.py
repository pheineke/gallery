import requests
from bs4 import BeautifulSoup
import os

class WallpaperDownloader:
    def __init__(self, url='https://wallhaven.cc/hot', save_folder='app/static/wallpapers'):
        self.url = url
        self.save_folder = save_folder
        os.makedirs(self.save_folder, exist_ok=True)

    def _is_wallpaper_downloaded(self, filename):
        """Check if the wallpaper has already been downloaded."""
        return os.path.exists(os.path.join(self.save_folder, filename))

    def download_wallpapers(self, num_wallpapers=5):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        wallpapers = soup.find_all('figure', class_='thumb')

        downloaded_count = 0
        new_wallpapers = []

        # Collect new wallpapers that haven't been downloaded yet
        for wallpaper in wallpapers:
            if downloaded_count >= num_wallpapers:
                break

            # Get the link to the full image
            img_url = wallpaper.find('a')['href']
            img_response = requests.get(img_url)
            img_soup = BeautifulSoup(img_response.text, 'html.parser')
            full_img_url = img_soup.find('img', id='wallpaper')['src']

            # Get the image filename
            img_name = full_img_url.split('/')[-1]

            # Check if the image has already been downloaded
            if self._is_wallpaper_downloaded(img_name):
                print(f'Skipped (already downloaded): {img_name}')
                continue

            new_wallpapers.append((full_img_url, img_name))
            downloaded_count += 1

        # Download new wallpapers
        for full_img_url, img_name in new_wallpapers:
            img_data = requests.get(full_img_url).content
            with open(os.path.join(self.save_folder, img_name), 'wb') as file:
                file.write(img_data)

            print(f'Downloaded: {img_name}')

# Example usage
if __name__ == "__main__":
    downloader = WallpaperDownloader('https://wallhaven.cc/hot')
    downloader.download_wallpapers(num_wallpapers=5)
