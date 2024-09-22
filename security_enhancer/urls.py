from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('upload/', views.upload_apk, name='upload_apk'),
    path('download/', views.download_page, name='download_page'),
]
