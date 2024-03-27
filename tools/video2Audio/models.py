from django.db import models

# Create your models here.
class Video(models.Model):
    video = models.FileField(upload_to='videos/', default='')
    videoID = models.AutoField(primary_key=True)
    def __str__(self):
        return self.video.name