# Generated by Django 3.2.3 on 2021-05-21 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suplier',
            name='GST_no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='OTP',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=50)),
                ('Lastname', models.CharField(max_length=50)),
                ('Gender', models.CharField(max_length=50)),
                ('Contact', models.CharField(max_length=50)),
                ('State', models.CharField(max_length=50)),
                ('City', models.CharField(max_length=50)),
                ('Address', models.CharField(max_length=50)),
                ('DOB', models.CharField(max_length=50)),
                ('Experience', models.CharField(max_length=50)),
                ('Qualfication', models.CharField(max_length=50)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
        ),
    ]
