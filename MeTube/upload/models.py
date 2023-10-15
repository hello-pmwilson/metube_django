from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=240)
    video_file = models.FileField(
        upload_to="videos/"
    )  # change this when folder is made
    upload_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = "upload"

    def __str__(self):
        return self.title
