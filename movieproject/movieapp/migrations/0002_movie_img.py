# Generated by Django 3.2.20 on 2023-08-03 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='demo', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
