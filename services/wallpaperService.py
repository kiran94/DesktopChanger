from services.fileIOService import fileIOService
from services.httpService import httpService
import json

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
    
    def storeLatestWallpaper(self, tempImageLocation):
        nextWallpaperUrl = self.__parseWallpaperJSON()
        nextWallpaper = self._httpService.get(nextWallpaperUrl)
        self._fileIOService.write(tempImageLocation, nextWallpaper)       

    # Returns the latest wallpaper from the URL.
    def __parseWallpaperJSON(self):
        images = self.__getLatestWallpapers()
        for i in range(0, len(images)):
            if images[i]["data"]["distinguished"] != "moderator":
                return images[i]["data"]["url"]
    
    # Returns a JSON of the URL. 
    def __getLatestWallpapers(self):
        pageJSON = self._httpService.get(self._url)
        pageJSON = json.loads(pageJSON)
        return pageJSON["data"]["children"]