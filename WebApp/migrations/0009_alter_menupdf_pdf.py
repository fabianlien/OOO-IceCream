# Generated by Django 3.2.15 on 2022-08-23 12:12

import cloudinary.models
import django.core.validators
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0008_alter_menupdf_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menupdf',
            name='pdf',
            field=cloudinary.models.CloudinaryField(max_length=255, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])]),
        ),
    ]
