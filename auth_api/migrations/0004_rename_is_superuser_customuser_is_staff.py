# Generated by Django 4.2.7 on 2023-11-10 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_api', '0003_remove_customuser_groups_remove_customuser_is_admin_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='is_superuser',
            new_name='is_staff',
        ),
    ]
