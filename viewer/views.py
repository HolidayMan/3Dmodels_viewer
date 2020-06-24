import os
import uuid
from django.core.files import File

from models_viewer.settings import BASE_DIR

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
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

        model = Model3D.objects.create(file=File(file), file_id=uuid.uuid4())

    if request.is_secure():
        link = 'https://' + request.get_host() + model.get_absolute_url()
    else:
        link = 'http://' + request.get_host() + model.get_absolute_url()

    response_data = {
        "file_id": model.file_id,
        "filename": os.path.split(model.file.name)[-1],
        "file_link": link,
        "file_size": model.file.size
    }
    return JsonResponse(response_data, status=200)


def show_model(request, file_id):
    model = get_object_or_404(Model3D, file_id=file_id)

    return render(request, 'viewer/view_page.html', context={
        "filename": os.path.split(model.file.name)[-1],
        "file_url": model.file.url
    })
