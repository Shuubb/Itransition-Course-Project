# Generated by Django 4.2.7 on 2023-11-17 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item_management', '0005_like_alter_item_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='like',
            name='created_at',
        ),
        migrations.AddField(
            model_name='item',
            name='optional_fields',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='topic',
            field=models.CharField(choices=[('Books', 'Books'), ('Whiskeys', 'Whiskeys'), ('Watches', 'Whatches'), ('Jewelary', 'Jewelary')], max_length=10),
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
    ]