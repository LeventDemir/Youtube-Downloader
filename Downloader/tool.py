import requests
from django.template.defaultfilters import filesizeformat
from django.http import HttpResponse
import pafy


def get_videos(video_name):

    base_url = 'https://www.googleapis.com/youtube/v3/search?'

    params = 'part=snippet&maxResults=6&q={}&type=video&key='.format(video_name)

    key = 'AIzaSyAwzVAkI6wXKV87KjgbN1qw_37UgvnNKUc'

    url = "{}{}{}".format(base_url, params, key)

    return requests.get(url).json()


def get_videos_by_token(video_name, token):

    base_url = 'https://www.googleapis.com/youtube/v3/search?'

    params = 'pageToken={}&part=snippet&maxResults=6&q={}&type=video&key='.format(token, video_name)

    key = 'AIzaSyAwzVAkI6wXKV87KjgbN1qw_37UgvnNKUc'

    url = "{}{}{}".format(base_url, params, key)

    return requests.get(url).json()


def download(video_url):

    video = pafy.new(video_url)
    stream = video.streams
    video_audio_streams = []

    for i in stream:
        video_audio_streams.append({
            'resolution': i.resolution,
            'extension': i.extension,
            'video_url': i.url + "&title=" + video.title
        })

    context = {
        'title': video.title,
        'streams': video_audio_streams,
        'video_id': video_url.split('=')[1]
    }

    return context
