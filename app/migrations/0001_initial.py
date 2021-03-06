# Generated by Django 3.0.3 on 2020-03-15 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flower',
            fields=[
                ('f_num', models.AutoField(primary_key=True, serialize=False)),
                ('f_name', models.CharField(max_length=16, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Userupimage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_icon', models.ImageField(upload_to='icons')),
            ],
            options={
                'db_table': 'flower',
            },
        ),
    ]
