import pymongo
import gridfs
import requests
from pymongo import MongoClient

from tmdb import TMDBDownloader


class mongodb:
    content_path = "content/"
    def __init__(self,ip,port):
        self.myclient = pymongo.MongoClient("mongodb",27017)
        self.db = self.myclient["posters"]
        self.tmdb_downloader = TMDBDownloader()
        self.fs = gridfs.GridFS(self.db)

    def mongo_conn(self):
        try:
            conn = MongoClient()
            self.database = conn["movies"]
            print("connected")
            return self.database
        except Exception as e:
            print("error in mongoDB connection ")

    # used GridFS to insert data into colum
    def insert_data(self, name):
        self.name = name
        movie_id = self.tmdb_downloader.getposterURL(name)[1]
        movie_url = self.tmdb_downloader.getposterURL(name)[0]
        # print("this is the movie url= " + str(movie_url))
        response = requests.get(movie_url, stream=True)
        state = False
        path = "upload/"
        # check if the poster exist by id
        if self.fs.exists({'my_id': movie_id}):
            print("already exist")
            state = True
            return state, "poster inserted"
        else:
            print("adding poster: " + str(self.name))
            print(response.raw)
            # if it doesn't exist then use put to insert into colum
            self.fs.put(response.raw, filename=self.name+".jpg", my_id=movie_id, html=movie_url, path = path + self.name+".jpg")
            return state

    # check if the poster exist before attempting delete
    def del_data(self, name):
        col = self.db["fs.files"]
        a = col.find()
        # print(a)
        for x in a:
            if x['filename'] == name + ".jpg":
                print("deleting " + str(x.get('filename')))
                col.delete_one(x)
                return "poster deleted"
            else:
                print("not found")


    def update_data(self):
        pass
    def search(self, filename):
        filename = filename + '.jpg'
        mycol = self.db["fs.files"]
        statment = False
        for x in mycol.find():
            if (filename == x['filename']):
                statment = True
                return statment
        return statment
    def read_data(self, filename):

        if (self.search(filename)):
            file = self.fs.find_one({"filename":filename+".jpg"}).read()
            with open(filename + ".jpg", 'wb') as w:
                w.write(file)
            return file
    # read data from fs.file colum
    def read_all_posters(self):
        posters = []
        col = self.db["fs.files"]
        x = col.find({})
        for document in x:
            print("poster: " + str(document['filename']))
            posters.append(document['filename'])
        print(posters)
        return posters
