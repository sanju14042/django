"""mahasiswa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from crud import views as crudviews
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import *




from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about),
    path('tambah/',crudviews.tambah, name='add-data'),
    path('editdata/<int:npm>',crudviews.edit),
    path('hapusdata/<int:npm>',crudviews.hapus),
    path('tambahdata/',crudviews.Data_mahasiswaCreateView, name='Data_mahasiswa_add'),
    path('<int:pk>/', crudviews.Data_mahasiswaUpdateView, name='Data_mahasiswa_change'),
    path('ajax/load-units/', crudviews.load_units, name='ajax_load_units'),
    path('drop/', crudviews.tambahdd),
    path('ddl/', crudviews.ddl),
    path('',crudviews.index),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



  