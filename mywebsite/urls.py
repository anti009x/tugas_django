
from django.urls import path
from mywebsite import views as Views

urlpatterns = [

    path('index/' , Views.index , name="views" ),
    path('berita/' , Views.berita1 , name="berita" ),
    path('berita2/' , Views.berita2 , name="berita2" )
]
