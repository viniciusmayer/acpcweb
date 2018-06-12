# Generated by Django 2.0.6 on 2018-06-12 18:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('trabalhos', '0002_auto_20180611_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='arquivo',
            name='paginas',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='evento',
            name='quando',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='trabalho',
            name='ano',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='trabalho',
            name='natureza',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='trabalho',
            name='titulo',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterUniqueTogether(
            name='evento',
            unique_together={('nome', 'quando')},
        ),
        migrations.AlterUniqueTogether(
            name='eventotrabalho',
            unique_together={('evento', 'trabalho', 'ordem')},
        ),
        migrations.AlterUniqueTogether(
            name='trabalho',
            unique_together={('ano', 'titulo', 'natureza')},
        ),
    ]