# Generated by Django 3.2.3 on 2021-06-24 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210617_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='addproduct',
            name='sup_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.suplier'),
        ),
    ]
