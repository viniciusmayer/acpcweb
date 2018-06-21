# Generated by Django 2.0.6 on 2018-06-18 12:07

from django.db import migrations, models
import django.db.models.deletion
from trabalhos.models import Natureza


class Migration(migrations.Migration):

    dependencies = [
        ('trabalhos', '0011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trabalho',
            name='natureza',
        ),
        migrations.RenameField(
            model_name='trabalho',
            old_name='nova_natureza',
            new_name='natureza',
        ),
    ]   