# Generated by Django 4.2.7 on 2023-11-13 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item_management', '0002_topic_alter_collection_topic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='name',
        ),
    ]