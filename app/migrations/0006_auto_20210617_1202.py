# Generated by Django 3.2.3 on 2021-06-17 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_catergory_suplier_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subcategory',
            old_name='Bname',
            new_name='Type',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='Bdescription',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='Bimg',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='Bprice',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='stock',
        ),
        migrations.CreateModel(
            name='AddProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bname', models.CharField(max_length=50)),
                ('Bprice', models.CharField(max_length=50)),
                ('Bdescription', models.CharField(max_length=150)),
                ('stock', models.CharField(default='available', max_length=50)),
                ('Bimg', models.ImageField(upload_to='img/')),
                ('is_created', models.DateTimeField(auto_now_add=True)),
                ('is_updated', models.DateTimeField(auto_now_add=True)),
                ('cat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.catergory')),
                ('subcat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.subcategory')),
            ],
        ),
    ]