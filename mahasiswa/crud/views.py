import os
import json as simplejson
from django.core.checks import messages
from django.forms.widgets import Media
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import *
from .forms import BiodataMhs, Data_mahasiswaForm

# Create your views here.

def index(request):
    hasil = Data_mahasiswa.objects.all()
    print(hasil) 
    data = {
        'data':hasil,
    }   
    return render(request,"index.html",data)  

def tambah(request):
    kerja = Pekerjaan.objects.all()
    unitobj = Unit.objects.all()
    form = BiodataMhs(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("/")
        pass
    return render(request,"tambahdata.html",{'form': form, "datakerja": kerja, "dataunit": unitobj})

def edit(request, npm):
    obj = get_object_or_404(Data_mahasiswa, npm = npm) 
  
    form = BiodataMhs(request.POST or None, request.FILES or None, instance = obj)
    if len(request.FILES) !=0:
        if len(obj.foto) > 0:
            os.remove(obj.foto.path)
        obj.foto = request.FILES['foto']
    obj.save()
    if form.is_valid(): 
        form.save() 
        return redirect("/")  
    #2 data = {
    #2     'mhs':obj,
    #2 }
    data = {'mhs':obj, 'form': form}
    return render(request,'editdata.html',data)

def hapus(request, npm):
    dt = Data_mahasiswa.objects.get(npm=npm)
    dt.delete()
    return redirect("/")

def tambahdd(request):
    kerja = Pekerjaan.objects.all()
    unitobj = Unit.objects.all()
    return render(request, 'tambahdrop.html', {"datakerja": kerja,"dataunit": unitobj})

def ddl(request):
    pekerjaan = Pekerjaan.objects.all()
    print(pekerjaan)
    return render(request, 'ddl.html', {'pekerjaan': pekerjaan})

def getdetails(request):
    pekerjaan_nama = request.GET['krj']
    print ("ajax " + str(pekerjaan_nama))

    result_set = []
    all_units = []

    answer = str(pekerjaan_nama[1:-1])
    selected_pekerjaan = Pekerjaan.objects.get(nama=answer)
    print ("selected pekerjaan name " + str(selected_pekerjaan))
    
    all_units = selected_pekerjaan.unit_set.all()
    for unit in all_units:
        print ("unit nama", str(unit.nama))
        result_set.append({'nama': unit.nama})
    return HttpResponse(simplejson.dumps(result_set),content_type='application/json')

# class Data_mahasiswaListView(ListView):
#     model = Data_mahasiswa
#     context_object_name = 'people'
#     template_name = 'listdd.html'
 
def Data_mahasiswaCreateView(request):
    form = Data_mahasiswaForm()
    if request.method == 'POST':
        form = Data_mahasiswaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Data_mahasiswa_add')
    return render(request, 'editdata.html', {'form': form})
 
 
def Data_mahasiswaUpdateView(request, pk):
    kerja = get_object_or_404(Data_mahasiswa, pk=pk)
    form = BiodataMhs(instance=kerja)
    if request.method == 'POST':
        form = BiodataMhs(request.POST, instance=kerja)
        if form.is_valid():
            form.save()
            return redirect('Data_mahasiswa_change', pk=pk)
    return render(request, 'editdata.html', {'form': form})
 
 #AJAX
def load_units(request):
    pekerjaan_id = request.GET.get('pekerjaan_id')
    units = Unit.objects.filter(pekerjaan_id=pekerjaan_id).all()
    return render(request, 'dropdown.html', {'units': units})
    # return JsonResponse(list(units.values('id', 'name')), safe=False)

# def foto_view(request):
#     if request.method == 'POST':
#         form = BiodataMhs(request.POST, request.FILES)
  
#         if form.is_valid():
#             form.save()
#             return redirect('success')
#     else:
#         form = BiodataMhs()
#     return render(request, 'uploadfoto.html', {'form' : form})
  
  
# def success(request):
#     return HttpResponse('successfully uploaded')




