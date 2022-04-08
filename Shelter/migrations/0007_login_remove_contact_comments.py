# Generated by Django 4.0.2 on 2022-04-07 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shelter', '0006_about_contact_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('comments', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='contact',
            name='comments',
        ),
    ]