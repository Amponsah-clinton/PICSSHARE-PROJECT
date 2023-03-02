from django.shortcuts import render,redirect
from .models import Category, Photo
from .forms  import PhotoForm,CategoryForm
# Create your views here.

def gallery(request):
# getting categories
    category  = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name  = category)
# categories end

    categories = Category.objects.all()
    context ={
    'categories':categories, 'photos':photos,
    }
    return render(request, 'gallery.html',context)

def viewPhoto(request,pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photo.html',{'photo': photo})

def addPhoto(request):
    form = PhotoForm()
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = PhotoForm()
            return redirect('/')
    return render(request, 'add.html',{'form':form})


def addCart(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            form = CategoryForm()
            return redirect('add')
    return render(request, 'addcart.html',{'form':form})
