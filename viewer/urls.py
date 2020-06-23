from django.urls import path
from .views import index, upload, show_model

urlpatterns = [
    path('', index),
    path('upload/', upload),
    path('models/<str:file_id>', show_model),
]
