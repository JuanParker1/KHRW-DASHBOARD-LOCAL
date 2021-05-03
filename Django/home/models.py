from django.db import models


class App(models.Model):

    title = models.CharField(max_length=200)
    app_id = models.IntegerField(default=1, unique=True)
    description = models.TextField(max_length=500)
    thumbnail = models.ImageField(upload_to="images")
    url = models.URLField(max_length=200, default="www.google.com")

    def __str__(self):
        return self.title
