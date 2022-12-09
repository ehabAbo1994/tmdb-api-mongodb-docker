from tmdb import TMDBDownloader
from mongodb import mongodb

def main():
    movie_name = "hitman"
    tmdb = TMDBDownloader()
    # tmdb.getURL()
    #tmdb.getposterURL(movie_name)
    # tmdb.download_image(movie_name)
    mdb = mongodb()
    mdb.insert_data(movie_name)
    #mdb.search(movie_name)
    #mdb.read_data(movie_name)
    #mdb.read_all_posters()
    # mdb.read_data()
    # mdb.del_data(movie_name)

if __name__ == '__main__':
    main()
