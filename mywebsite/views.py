from django.shortcuts import render

# Create your views here.


def index(request):
   context = {
    'name': 'Rizky'
    }
   
   return render (request,'index.html',context)

def berita1(request):
    return render (request,'berita1.html')

def berita2(request):
    return render (request,'berita2.html')