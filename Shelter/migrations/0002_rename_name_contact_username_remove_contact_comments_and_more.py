# Generated by Django 4.0.2 on 2022-04-05 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shelter', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='name',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='email',
        ),
    ]
