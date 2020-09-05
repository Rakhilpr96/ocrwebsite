from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .forms import *
import os
from PIL import Image as Img
import pytesseract

# Create your views here.

def upload(request):
    
    if request.method == 'POST': 
        form = ImageForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return redirect('result') 
    else: 
        form = ImageForm() 
    return render(request, 'index.html', {'form' : form}) 
  

# program to view 

def display_images(request): 

	if request.method == 'GET': 
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            img = Image.objects.get(name="photo")
            imdir = os.path.join(BASE_DIR,'media/') + img.Upload_Img.name
            img = Img.open(imdir)
            text = pytesseract.image_to_string(img,lang='eng')
            if os.path.exists(imdir):
                os.remove(imdir)
            Image.objects.all().delete()
            return render(request,'result.html',{'text' : text})
					


