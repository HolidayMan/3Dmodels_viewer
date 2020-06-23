import os
import uuid
from django.core.files import File

from models_viewer.settings import BASE_DIR

from django.shortcuts import render
from django.http import HttpResponse
from .models import Model3D


def index(request):
    return render(request, 'viewer/index.html')


def upload(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed", 403)
    file = request.FILES['file']
    with open(os.path.join(BASE_DIR, "models", file.name), 'wb') as f:
        for chunk in file.chunks():
            f.write(chunk)

        Model3D.objects.create(file=File(file), file_id=uuid.uuid4())

    return HttpResponse("Hello world", 200)


def show_model(request, file_id):
    model = Model3D.objects.get(file_id=file_id)

    return render(request, 'viewer/view_page.html', context={"filename": model.file.name, "file_url": model.file.url})
