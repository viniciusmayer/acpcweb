# Generated by Django 2.0.6 on 2018-06-15 23:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trabalhos', '0005_trabalho_anofim'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trabalho',
            old_name='anoFim',
            new_name='ano_fim',
        ),
    ]
