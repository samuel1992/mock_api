# Generated by Django 3.2.5 on 2021-07-16 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mockresponse',
            old_name='http_method',
            new_name='path',
        ),
    ]
