# Generated by Django 3.1.7 on 2021-05-04 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20210504_1347'),
    ]

    operations = [
        migrations.RenameField(
            model_name='members',
            old_name='package',
            new_name='plan',
        ),
    ]