# Generated by Django 4.2.5 on 2023-10-02 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0003_alter_detailsmodel_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detailsmodel',
            name='address',
        ),
    ]
