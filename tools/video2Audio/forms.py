from django import forms
from .models import Video  # assuming you have a Video model

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['video_file']  # replace with your actual field name