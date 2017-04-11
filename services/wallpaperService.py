import json
import random 
import re 
from services.fileIOService import fileIOService
from services.httpService import httpService

# Services for Wallpaper operations
class wallpaperService:

    # URL for the request to get a wallpaper.
    _url = None

    #File IO Service.
    _fileIOService = None

    #Http Service.
    _httpService = None

    #Initilises an instance of the wallpaper service and injects the values. 
    def __init__(self, url, fileIOService, httpService):
        self._url = url
        self._fileIOService = fileIOService
        self._httpService = httpService        
    
    # Gets and writes the latest wallpaper. 
    def storeLatestWallpaper(self, tempImageLocation):
        nextWallpaperUrl = self.__parseWallpaperJSON()
        nextWallpaper = self._httpService.get(nextWallpaperUrl)
        self._fileIOService.write(tempImageLocation, nextWallpaper)       

    # Returns the latest wallpaper from the URL and filters any invalid links. 
    def __parseWallpaperJSON(self):
        images = self.__getLatestWallpapers()
        realPostIndex = 0
        for i in range(0, len(images)):
            if images[i]["data"]["distinguished"] != "moderator":
                realPostIndex = i
                break
        
        wallpaperURL = None
        while wallpaperURL == None:            
            index = random.randrange(realPostIndex, len(images)-1)
            current = images[index]["data"]["url"]

            if (current != "" and re.match("(.)*jpg$", current) != None):
                wallpaperURL = current
                break  
     
        return wallpaperURL
    
    # Returns a JSON of the URL. 
    def __getLatestWallpapers(self):
        pageJSON = self._httpService.get(self._url)
        pageJSON = json.loads(pageJSON)
        return pageJSON["data"]["children"]