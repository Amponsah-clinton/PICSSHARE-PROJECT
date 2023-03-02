from django.forms import ModelForm
from .models import Category, Photo

class PhotoForm(ModelForm):
    class Meta:
        fields = '__all__'
        model = Photo

class CategoryForm(ModelForm):
    class Meta:
        fields = '__all__'
        model = Category