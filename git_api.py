import urllib.request as url
import json

VERSION = "0.0.3 - Drawing Board Functional release"
APIURL = "http://api.github.com/repos/"

def vercheck() -> str:
    return str(VERSION)

def getData(repoURL):
    with url.urlopen(APIURL + repoURL + "/releases") as data_raw:
        repoData = json.loads(data_raw.read().decode())
        return repoData

def getLastestReleaseData(repoData):
    return repoData[0]

def getAuthor(releaseData):
    return releaseData['author']['login']
    
def getReleaseName(releaseData):
    return releaseData['name']

def getReleaseDate(releaseData):
    return releaseData['published_at']

def getReleaseFileName(releaseData): #still needs to get datetime shit here, and multiple files
    return releaseData['assets'][0]['name']

def getReleaseFileURL(releaseData):
    return releaseData['assets'][0]['browser_download_url']

def getAssetsSize(releaseData):
    return len(releaseData['assets'])
