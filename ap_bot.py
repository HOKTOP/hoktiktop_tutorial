import requests
import json
from pytube import YouTube

def geturlfacebook(url):
    url2 = "https://facebook-reel-and-video-downloader.p.rapidapi.com/app/main.php"
    querystring = {"url":f"{url}"}
    headers = {
	"X-RapidAPI-Key": "yout key",
	"X-RapidAPI-Host": "facebook-reel-and-video-downloader.p.rapidapi.com"
    }
    response = requests.request("GET", url2, headers=headers, params=querystring)
    jsondata = json.loads(response.text)
    #namevideo=jsondata['title']
    hdvideurl = jsondata['links']['Download High Quality']
    response.close()

    return(hdvideurl)


def urltube(url):
     data=YouTube(url).streams.filter(progressive=True,file_extension='mp4').get_highest_resolution().url
     return(data)

def urlinsta(url):
    url2 = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"
    querystring = {"url":f"{url}"}
    headers = {
	"X-RapidAPI-Key": "yout key",
	"X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
    }
    response = requests.request("GET", url2, headers=headers, params=querystring)
    jsondata=json.loads(response.text)
    urla = jsondata['media'] 
    response.close()

    return(urla)
def urltiktok(url):
    url2 = "https://tiktok-video-no-watermark2.p.rapidapi.com/"
    querystring = {"url":"https://www.tiktok.com/@tiktok/video/7106658991907802411","hd":"0"}
    headers = {
	"X-RapidAPI-Key": "yout key",
	"X-RapidAPI-Host": "tiktok-video-no-watermark2.p.rapidapi.com"
    }
    response = requests.request("GET", url2, headers=headers, params=querystring)
    jsondata=json.loads(response.text)
    urla = jsondata['data']['play'] 
    response.close()
    return(urla)

