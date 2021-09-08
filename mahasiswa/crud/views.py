from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import BiodataMhs
import json as simplejson

# Create your views here.

def index(request):
    hasil = Data_mahasiswa.objects.all()
    print(hasil) 
    data = {
        'data':hasil,
    }   
    return render(request,"index.html",data)  

def tambah(request):
    form = BiodataMhs(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("/")
        pass
    return render(request,"tambahdata.html",{'form': form})

# def edit(request, npm):
#     data = Data_mahasiswa.objects.get(npm=npm)
#     return render(request,'editdata.html',{'data':data})

def edit(request, npm):
    obj = get_object_or_404(Data_mahasiswa, npm = npm) 
  
    form = BiodataMhs(request.POST or None, instance = obj)
    if form.is_valid(): 
        form.save() 
        return redirect("/")  
    data = {
        'mhs':obj,
    }
    return render(request,'editdata.html',data)

def hapus(request, npm):
    dt = Data_mahasiswa.objects.get(npm=npm)
    dt.delete()
    return redirect("/")

def tambahdd(request):
    kerja = Pekerjaan.objects.all()
    print(kerja)
    return render(request, 'tambahdd.html', {'kerja': kerja})

def getdetails(request):
    #country_name = request.POST['country_name']
    kerja_name = request.GET['krj']
    print ("ajax " + str(kerja_name))

    result_set = []
    all_units = []

    answer = str(kerja_name[1:-1])
    selected_kerja = Pekerjaan.objects.get(name=answer)
    print ("selected kerja name " + str(selected_kerja))
    
    all_units = selected_kerja.unit_set.all()
    for unit in all_units:
        print ("unit name", str(unit.name))
        result_set.append({'name': unit.name})
    return HttpResponse(simplejson.dumps(result_set), mimetype='application/json',content_type='application/json')





