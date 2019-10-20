from bs4 import BeautifulSoup as bs
import requests
import json
def youtube_crawler(url):
    base = "https://www.youtube.com/results?search_query="
    r = requests.get(base+url)
    page = r.text
    soup=bs(page,'html.parser')
    vids = soup.findAll('a',attrs={'class':'yt-uix-tile-link'})
    videolist=[]
    videolistjson = []
    for v in vids:
        tmp = 'https://www.youtube.com' + v['href']
        videolist.append(tmp)
    for i in range(len(videolist)):
        video = {}
        video['id'] = videolist[i].split('=')[1]
        videolistjson.append(video)
    
    videolistjson = json.dumps(videolistjson)
    return videolistjson