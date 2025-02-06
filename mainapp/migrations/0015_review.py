# Generated by Django 5.0.6 on 2024-09-09 19:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_delete_review'),
        ('user_app', '0003_alter_userprofile_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=4, verbose_name='Rating from 1 to 5')),
                ('text', models.TextField(verbose_name='Review text')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('user_profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_app.userprofile')),
            ],
        ),
    ]
