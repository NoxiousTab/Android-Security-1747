from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_apk, name='upload_apk'),
]
