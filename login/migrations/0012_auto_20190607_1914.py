# Generated by Django 2.2.1 on 2019-06-07 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0011_user_permission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=20, unique='true'),
        ),
    ]
