import os 
import uuid
from services.desktopService import desktopService
from services.fileIOService import fileIOService
from services.httpService import httpService
from services.wallpaperService import wallpaperService

redditBaseUrl = "https://www.reddit.com"
redditSubUrl = "Wallpaper"
redditSubFormat = "json"
redditSubCount = 20

redditUrl = "{}/r/{}/.{}?count={}".format(redditBaseUrl, redditSubUrl, redditSubFormat, redditSubCount)

tempLocFolder = "/tmp/desktopchanger/"
tempLoc = "{}{}.jpg".format(tempLocFolder,uuid.uuid4())

if not os.path.exists(tempLocFolder):
    os.makedirs(tempLocFolder)

http = httpService()
fileIO = fileIOService()
desktop = desktopService()

wallpaper = wallpaperService(redditUrl, fileIO, http)
wallpaper.storeLatestWallpaper(tempLoc)
desktop.changeDesktop(tempLoc)
os.remove(tempLoc)