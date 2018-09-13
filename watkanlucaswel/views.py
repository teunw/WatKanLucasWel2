from django.db.models import Count
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render
from watkanlucaswel.models import WKLWImage


def index(request):
    return render(request, 'index.html')


def randomimage(request):
    image = WKLWImage.objects.order_by('?').first()  # type: WKLWImage
    return HttpResponse(image.imageFile)
