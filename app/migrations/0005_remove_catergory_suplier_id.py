# Generated by Django 3.2.3 on 2021-06-11 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_catergory_subcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catergory',
            name='suplier_id',
        ),
    ]