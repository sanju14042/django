# Generated by Django 3.2.7 on 2021-09-06 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='data_mahasiswa',
            name='jenisk',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
