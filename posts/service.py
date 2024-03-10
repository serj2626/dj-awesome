from bs4 import BeautifulSoup
import requests


def get_data_for_post(post):

    website = requests.get(post.url)

    sourcecode = BeautifulSoup(website.text, 'html.parser')
    find_image = sourcecode.select(
        'meta[content^="https://live.staticflickr.com/"]')
    image = find_image[0]['content']

    find_title = sourcecode.select('h1.photo-title')
    title = find_title[0].text.strip()

    find_artist = sourcecode.select('a.owner-name')
    artist = find_artist[0].text.strip()

    return {
        'image': image,
        'title': title,
        'artist': artist
    }


def get_path_for_icon(instance, filename):
    return f'icons/{instance.slug}/{filename}'
