from django.db import models


class Model3D(models.Model):
    file = models.FileField(upload_to="models/")
    file_id = models.CharField(max_length=256)

    def get_absolute_url(self):
        return f"/viewer/models/{self.file_id}"
