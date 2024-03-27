from django import forms
from django.forms import ModelForm

# create a form
class VideoForm(forms.Form):
    video = forms.FileField(label='Select a video file')