# Generated by Django 2.0.4 on 2018-12-27 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trabalhos', '0014_auto_20180625_2210'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='arquivo',
            options={'ordering': ['arquivo']},
        ),
        migrations.AlterModelOptions(
            name='entidade',
            options={'ordering': ['nome']},
        ),
        migrations.AlterModelOptions(
            name='evento',
            options={'ordering': ['nome']},
        ),
        migrations.AlterModelOptions(
            name='eventotrabalho',
            options={'ordering': ['ordem']},
        ),
        migrations.AlterModelOptions(
            name='natureza',
            options={'ordering': ['nome']},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['nome']},
        ),
        migrations.AlterModelOptions(
            name='trabalho',
            options={'ordering': ['ano', 'tag', 'titulo']},
        ),
        migrations.AddField(
            model_name='arquivo',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='entidade',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='evento',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='eventotrabalho',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='natureza',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='trabalho',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='trabalho',
            name='ano_fim',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trabalho',
            name='arquivo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='trabalhos.Arquivo'),
        ),
        migrations.AlterField(
            model_name='trabalho',
            name='entidade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='trabalhos.Entidade'),
        ),
        migrations.AlterField(
            model_name='trabalho',
            name='natureza',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='trabalhos.Natureza'),
        ),
    ]