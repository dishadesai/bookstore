# Generated by Django 3.2.3 on 2021-06-29 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_addtocart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addtocart',
            name='QTY',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='addtocart',
            name='Subtotal',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='addtocart',
            name='Total',
            field=models.IntegerField(default=0),
        ),
    ]
