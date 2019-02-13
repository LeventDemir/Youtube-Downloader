from django.shortcuts import render
from .tool import get_videos, get_videos_by_token, download

def Index(request):

    video_name = request.GET.get('video_name')

    if video_name:
        videos = get_videos(video_name)
        
        nextPage = ''

        if videos['pageInfo']['totalResults'] == 0:
            context = {'notFound': 'There is no result'}
            return render(request, 'index.html', context)

        elif 'nextPageToken' in videos:
            nextPage = videos['nextPageToken']

        context = {
            'videos': videos['items'],
            'next': nextPage,
            'video_name': video_name
        }
    
        return render(request, 'index.html', context)

    return render(request, 'index.html')


def ChangePage(request, token, keyword):

    videos = get_videos_by_token(keyword, token)

    prev = ''

    if 'prevPageToken' in videos:
        prev = videos['prevPageToken']

    context = {
        'videos': videos['items'],
        'next': videos['nextPageToken'],
        'prev': prev,
        'video_name': keyword
    }

    return render(request, 'index.html', context)


def Download(request, id):

    video_url = 'https://www.youtube.com/watch?v={}'.format(id)

    context = download(video_url)

    return render(request, 'download.html', context)
