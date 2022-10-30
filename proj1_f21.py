#########################################
##### Name:        Ziyan Wang       #####
##### Uniqname:       wziyan        #####
#########################################
import json
from pydoc import allmethods
import requests
import os
import webbrowser
# f = open(r"C:\Users\63476\Desktop\SI507\proj1\sample_json.json")
# sample_data = json.loads(f.read())
# print(sample_data[0]["trackName"])


class Media:
    def __init__(self, title="No Title", author="No Author", release_year="No Release Year", url="No URL", json =None):
        if json is None:
            self.title = title
            self.author = author
            self.release_year = release_year
            self.url = url
        else:
            self.title = json["collectionName"]
            self.author = json["artistName"]
            self.release_year = json["releaseDate"][:4]
            self.url = json["collectionViewUrl"]

    def info(self):
        return self.title + " by " + self.author + " (" + str(self.release_year) + ")"

    def length(self):
        return 0

class Song(Media):
    def __init__(self, title="No Title", author="No Author", release_year="No Release Year", url="No URL", 
    album = "No Album", genre="No Genre", track_length = 0, json =None):
        super().__init__(title, author, release_year, url, json )
        if json is None:
            self.album = album
            self.genre = genre
            self.track_length = track_length
        else:
            self.title = json["trackName"]
            self.url = json["trackViewUrl"]
            self.album = json["collectionName"]
            self.genre = json["primaryGenreName"]
            self.track_length = json["trackTimeMillis"]

    def info(self):
        return self.title + " by " + self.author + " (" + str(self.release_year) + ")" + " [" + self.genre + "]"
    
    def length(self):
        return round(self.track_length/1000) 

class Movie(Media):
    def __init__(self, title="No Title", author="No Author", release_year="No Release Year", url="No URL",
    rating = "No Rating", movie_length = 0, json =None):
        super().__init__(title, author, release_year, url, json )
        if json  is None:
            self.rating = rating
            self.movie_length = movie_length
        else:
            self.title = json["trackName"]
            self.url = json["trackViewUrl"]
            self.rating = json["contentAdvisoryRating"]
            self.movie_length  = json["trackTimeMillis"]
    def info(self):
        return self.title + " by " + self.author + " (" + str(self.release_year) + ")" + " [" + self.rating + "]"
    
    def length(self):
        return round(self.movie_length/1000/60)


if __name__ == "__main__":
    #PART 3
    PART3_URL = "https://itunes.apple.com/search?term=bon+jovi"
    resp3 = requests.get(PART3_URL)
    results_part3_obj = resp3.json()
    part3List = results_part3_obj["results"]
    # print(part3List)



    #Part 4
    BASE_URL = "https://itunes.apple.com/search?term="
    print('Enter a search term, or "exit" to quit:')
    tail = input()
    if tail == "exit":
        print("Bye!")
        os._exit(0)
    
    def queryByTail(tail):
        resp = requests.get(BASE_URL+tail)
        results_obj = resp.json()
        lis = results_obj["results"]

        movies = []
        songs = []
        others = []
        for item in lis:
            kind = item["kind"]
            if kind == "song":
                songs.append(Song(json=item))
            elif "movie" in kind:
                movies.append(Movie(json=item))
            else:
                others.append(Media(json=item))
        
        cnt = 1
        allMedia = songs+movies+others

        # while cnt<=totalN:
        #     curMedia = allMedia[cnt-1]
        print("SONGS")
        for item in songs:
            print(str(cnt)+" "+item.info())
            cnt+=1
        print("\n")

        print("MOVIES")
        for item in movies:
            print(str(cnt)+" "+item.info())
            cnt+=1
        print("\n")       

        print("OTHER MEDIA")
        for item in others:
            print(str(cnt)+" "+item.info())
            cnt+=1
        return allMedia

    allMedia = queryByTail(tail)

    queryAgain = 1
    while queryAgain != "exit":
        print("Enter a number for more info, or another search term, or exit: ")
        queryAgain = input()
        if queryAgain == "exit":
            print("Bye!")
            os._exit(0)
        elif queryAgain.isdigit():
            webbrowser.open(allMedia[int(queryAgain)-1].url)
        else:
            allMedia = queryByTail(queryAgain)

    # print(results_obj)
    # your control code for Part 4 (interactive search) should go here

