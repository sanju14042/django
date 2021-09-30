from django.db import models
from .validators import validate_file_size

# Create your models here.
class Pekerjaan(models.Model):
    nama = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nama

    def __unicode__(self):


        return u'%s' % (self.name)

class Unit(models.Model):
    nama = models.CharField(max_length=255, null=True, blank=True)
    pekerjaan = models.ForeignKey(Pekerjaan, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama

    def __unicode__(self):
        return u'%s' % (self.name)
        
class Data_mahasiswa(models.Model):
    npm = models.CharField(primary_key=True, max_length=15)
    nama = models.CharField(max_length=100, blank=True, null=True)
    tgl_lahir = models.DateField(blank=True, null=True)
    alamat = models.CharField(max_length=200, blank=True, null=True)
    sex_choices = (
        ('Laki-laki', 'Laki-laki'),
        ('Perempuan', 'Perempuan'),
        )
    jenisk = models.CharField(max_length=12, choices=sex_choices, blank=True, null=True)
    pekerjaan = models.ForeignKey(Pekerjaan, on_delete=models.SET_NULL, blank=True, null=True)
    unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, blank=True, null=True)
    foto = models.ImageField(upload_to='images/',  validators=[validate_file_size])

    class Meta:
        db_table = 'dt_mahasiswa'

