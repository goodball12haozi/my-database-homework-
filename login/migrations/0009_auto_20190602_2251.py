# Generated by Django 2.2.1 on 2019-06-02 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_auto_20190602_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='c_time',
            field=models.CharField(max_length=20),
        ),
    ]