# Generated by Django 3.0.3 on 2020-03-16 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200316_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userupimage',
            name='u_icon',
            field=models.ImageField(upload_to='img/'),
        ),
    ]