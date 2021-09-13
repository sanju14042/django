import os
from django.core.checks import messages
from django.forms.widgets import Media
from django.http import HttpResponse
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
    return render(request,"tambahdata.html",{'form': form, 'datakerja': kerja,'dataunit': unitobj})

# def edit(request, npm):
#     data = Data_mahasiswa.objects.get(npm=npm)
#     return render(request,'editdata.html',{'data':data})

def edit(request, npm):
    obj = get_object_or_404(Data_mahasiswa, npm = npm) 
  
    form = BiodataMhs(request.POST or None, instance = obj)
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
    data = {'mhs':obj}
    return render(request,'editdata.html',data)

def hapus(request, npm):
    dt = Data_mahasiswa.objects.get(npm=npm)
    dt.delete()
    return redirect("/")

def tambahdd(request):
    kerja = Pekerjaan.objects.all()
    unitobj = Unit.objects.all()
    return render(request, 'tambahdrop.html', {'datakerja': kerja,'dataunit': unitobj})

# def getdetails(request):
#     kerja_name = request.GET['krj']
#     print ("ajax " + str(kerja_name))

#     result_set = []
#     all_units = []

#     answer = str(kerja_name[1:-1])
#     selected_kerja = Pekerjaan.objects.get(name=answer)
#     print ("selected kerja name " + str(selected_kerja))
    
#     all_units = selected_kerja.unit_set.all()
#     for unit in all_units:
#         print ("unit name", str(unit.name))
#         result_set.append({'name': unit.name})
#     return HttpResponse(simplejson.dumps(result_set), mimetype='application/json',content_type='application/json')

class Data_mahasiswaListView(ListView):
    model = Data_mahasiswa
    context_object_name = 'people'
    template_name = 'listdd.html'
 
class Data_mahasiswaCreateView(CreateView):
    model = Data_mahasiswa
    form_class = Data_mahasiswaForm
    template_name = 'tambahform.html'
    success_url = reverse_lazy('Data_mahasiswa_changelist')
 
 
class Data_mahasiswaUpdateView(UpdateView):
    model = Data_mahasiswa
    form_class = Data_mahasiswaForm
    template_name = 'tambahform.html'
    success_url = reverse_lazy('Data_mahasiswa_changelist')
 
 
def load_units(request):
    pekerjaan_id = request.GET.get('pekerjaan')
    units = Unit.objects.filter(pekerjaan_id=pekerjaan_id).order_by('name')
    return render(request, 'dropdown.html', {'units': units})

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




