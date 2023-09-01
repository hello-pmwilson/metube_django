from django import forms
from .models import Video

class VideoUploadForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'video_file']

# class VideoUploadForm(forms.Form):
#     title = forms.CharField(label = "Title", max_length=100)