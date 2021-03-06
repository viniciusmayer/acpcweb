# Generated by Django 2.0.4 on 2018-04-24 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arquivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(editable=False, max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trabalho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.PositiveSmallIntegerField(editable=False)),
                ('titulo', models.CharField(editable=False, max_length=255)),
                ('natureza', models.CharField(editable=False, max_length=255)),
                ('arquivo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='trabalhos.Arquivo')),
            ],
        ),
    ]
