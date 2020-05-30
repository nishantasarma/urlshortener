from django.db import models

# Create your models here.
class UrlMap(models.Model):

    longurl = models.CharField(max_length=30, primary_key=True, null=False, blank=False)
    shorturl = models.CharField(max_length=4)


    def __str__(self):
        return str(self.longurl) + ',' + str(self.shorturl)
