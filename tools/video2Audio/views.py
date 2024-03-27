from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import VideoForm
def index(request):
    video = VideoForm()
    submitted = False
    if request.method == 'POST':
        video = VideoForm(request.POST, request.FILES)
        if video.is_valid():
            # file is saved
            video.save()
            return HttpResponseRedirect('/video2Audio?submitted=True')
    else:
        video = VideoForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'video2Audio/index.html', {'form': video}, {'submitted': submitted})
