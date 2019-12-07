import urllib.request as url
import json

VERSION = "0.1.1 - Alpha release"
APIURL = "http://api.github.com/repos/"

def vercheck() -> str:
    return str(VERSION)

def getData(repoURL):
    try:
        with url.urlopen(APIURL + repoURL + "/releases") as data_raw:
            repoData = json.loads(data_raw.read().decode())
            return repoData
    except:
        return None

def getLastestReleaseData(repoData):
    return repoData[0]

def getAuthor(releaseData):
    return releaseData['author']['login']
    
def getReleaseName(releaseData):
    return releaseData['name']

def getReleaseDate(releaseData):
    return releaseData['published_at']

def getAssetsSize(releaseData):
    return len(releaseData['assets'])
    
#still needs to get datetime shit here
def getAssets(releaseData):
    return releaseData['assets']

def getReleaseFileName(asset): 
    return asset['name']

def getReleaseFileURL(asset):
    return asset['browser_download_url']


