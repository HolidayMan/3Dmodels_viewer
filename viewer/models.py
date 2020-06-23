from django.db import models


class Model3D(models.Model):
    file = models.FileField(upload_to="models/")
    link = models.CharField(max_length=256)

