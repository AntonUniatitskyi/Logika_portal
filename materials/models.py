from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Materials(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def get_youtube_url(self):
        url = self.url
        for i in url:
            if i != "=":
                url=url.replace(i,'')
            else:
                url=url.replace(i,'')
                break
        print(url)
        return f'https://www.youtube.com/embed/{url}'
    
    def youtube_id(self):
        from urllib.parse import urlparse, parse_qs
        query = urlparse(self.url).query
        return parse_qs(query).get("v", [None])[0]