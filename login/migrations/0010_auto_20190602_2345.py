# Generated by Django 2.2.1 on 2019-06-02 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_auto_20190602_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=20),
        ),
    ]
