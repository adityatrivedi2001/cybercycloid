# Generated by Django 2.2.14 on 2021-04-03 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_teammates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammates',
            name='img',
            field=models.ImageField(upload_to='static/upload'),
        ),
    ]
