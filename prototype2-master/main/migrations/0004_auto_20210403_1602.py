# Generated by Django 2.2.14 on 2021-04-03 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210403_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammates',
            name='img',
            field=models.ImageField(upload_to='assests/upload'),
        ),
    ]