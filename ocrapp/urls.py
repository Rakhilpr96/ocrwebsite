from django.urls import path
from . import views

urlpatterns = [
    path('',views.upload,name='imgupload'),
    path('result',views.display_images, name = 'result'),
    ]