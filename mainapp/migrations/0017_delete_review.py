# Generated by Django 5.0.6 on 2024-09-10 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0016_review_is_clean_service_review_is_pleasant_master_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Review',
        ),
    ]
