# File crud/views.py
from django import forms
from django.db.models import fields
from django.db.models.fields import files
from .models import Data_mahasiswa, Unit

class BiodataMhs(forms.ModelForm):
    class Meta:
        model = Data_mahasiswa
        fields = "__all__"
        error_messages = {
            'npm': {
                'required': 'Anda harus mengisi form NPM'
            },
            'nama' : {
                'required': "Anda harus mengisi form Nama"
            },
            'tgl_lahir' : {
                'required': "Anda harus menset form Tanggal lahir"
            },
            'alamat':{
                'required': "Anda harus mengisi form Alamat"
            },            
            'jenisk':{
                'required': "Anda harus mengisi form Jenis kelamin"
            }
            
        }
    def  __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['unit'].queryset = Unit.objects.none()

        if 'pekerjaan' in self.data:
            try:
                pekerjaan_id = int(self.data.get('pekerjaan'))
                self.fields['unit'].queryset = Unit.objects.filter(pekerjaan_id=pekerjaan_id).order_by('nama')
            except (ValueError, TypeError):
                pass # inva;id input from the  client; ignore and fallback to empty Unit queryset
        elif self.instance.pk:
            self.fields['unit'].queryset = self.instance.pekerjaan.unit_set.order_by('nama')

class Data_mahasiswaForm(forms.ModelForm):
    class Meta :
        model = Data_mahasiswa
        fields = '__all__'

    def  __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['unit'].queryset = Unit.objects.none()

        if 'pekerjaan' in self.data:
            try:
                pekerjaan_id = int(self.data.get('pekerjaan'))
                self.fields['unit'].queryset = Unit.objects.filter(pekerjaan_id=pekerjaan_id).order_by('nama')
            except (ValueError, TypeError):
                pass # inva;id input from the  client; ignore and fallback to empty Unit queryset
        elif self.instance.pk:
            self.fields['unit'].queryset = self.instance.pekerjaan.unit_set.order_by('nama')

