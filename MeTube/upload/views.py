from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import VideoUploadForm


# Create your views here.
def upload(request):
    return render(request, "upload/upload.html")


def upload_video(request):
    if request.method == "POST":
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Process Form Data###
            form.save()
            return HttpResponseRedirect(reverse("home:home"))

    else:
        form = VideoUploadForm()
        # return render(request, 'upload_video.html', {'form' : form})
        return render(request, "upload/upload_video.html", {"form": form})
