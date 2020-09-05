from django import forms 
from .models import *

class ImageForm(forms.ModelForm): 

	class Meta: 
		model = Image
		fields = ['name', 'Upload_Img'] 
		widgets = {'name':forms.HiddenInput()}
		labels = {
			'Upload_Img':'Upload Image'
		}
