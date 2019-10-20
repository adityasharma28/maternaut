from django.shortcuts import render
from scrapers import youtube_crawl
import json

def learn(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        video_ids = youtube_crawl.youtube_crawler(query)
        video_ids = json.loads(video_ids)
        return render(request, 'learn/learn.html', {'video_ids': video_ids})
    return render(request, 'learn/learn.html')