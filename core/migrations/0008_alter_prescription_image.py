# Generated by Django 3.2.13 on 2023-01-03 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_prescription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='image',
            field=models.ImageField(upload_to='image/prescription'),
        ),
    ]
