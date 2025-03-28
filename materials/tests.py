from django.test import TestCase

# Create your tests here.
def get_youtube_url():
    url = 'https://www.youtube.com/watch?v=4WBZw0IyK20'
    for i in url:
        if i != "=":
            url=url.replace(i,'')
        else:
            url=url.replace(i,'')
            break
    return f'https://www.youtube.com/embed/{url}'


print(get_youtube_url())