import requests
import os
from dotenv import load_dotenv

load_dotenv()


class TMDBDownloader:

    def __init__(self):
        self.api_key = os.getenv('API_KEY')
        self.api_token = os.getenv('ACCESS_TOKEN')
        self.api_url = os.getenv('URL')
        self.CONFIG_PATTERN = 'http://api.themoviedb.org/3/configuration?api_key={key}'
        IMG_PATTERN = 'http://api.themoviedb.org/3/movie/{imdbid}/images?api_key={key}'


    def getposterURL(self, name):
        jpg_path = ''
        # the basic image url we need to add the poster backdroppath to the end to get the poster
        image_base_url = f'https://image.tmdb.org/t/p/w1280{jpg_path}'
        # used to search for the movie in tmdb by name
        search_url = f'https://api.themoviedb.org/3/search/movie?query={name}&api_key={self.api_key}'
        request = requests.get(search_url)
        jpg_path = request.json()
        # the backdrop_path to add to the end of the image_base_url
        backdrop_path = jpg_path.get('results')[0].get('backdrop_path')
        # get_id = the movie id by tmdb
        get_id = jpg_path.get('results')[0].get('id')
        url = (image_base_url + backdrop_path)
        print(url)
        return url, get_id

    '''
    this function downloads the posters locale.
    *** remove the get_id from getposterURL for this function to work ***
    '''

    def download_image(self, name):
        search_url = f'https://api.themoviedb.org/3/search/movie?query={name}&api_key={self.api_key}'
        response = requests.get(self.getposterURL(name))
        file = open(name + ".jpg", "wb")
        file.write(response.content)
        file.close()
