# Generated by Django 4.1.3 on 2022-11-24 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='image')),
                ('name', models.CharField(max_length=350)),
                ('desc', models.TextField()),
            ],
        ),
    ]
