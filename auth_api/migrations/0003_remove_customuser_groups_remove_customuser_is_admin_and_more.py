# Generated by Django 4.2.7 on 2023-11-10 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_api', '0002_alter_customuser_groups'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='user_permissions',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]