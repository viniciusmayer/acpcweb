# Generated by Django 2.0.6 on 2018-06-17 20:39

from django.db import migrations, models
import django.db.models.deletion
from trabalhos.models import Tag


def migrarTags(apps, schema_editor):
    trabalhos = apps.get_model('trabalhos', 'trabalho')
    tags = apps.get_model('trabalhos', 'tag')
    for trabalho in trabalhos.objects.all().iterator():
        _tags = tags.objects.filter(nome=trabalho.tag)
        if len(_tags) == 0:
            tag = Tag()
            tag.nome = trabalho.tag
            tag.save()


def associarTags(apps, schema_editor):
    trabalhos = apps.get_model('trabalhos', 'trabalho')
    tags = apps.get_model('trabalhos', 'tag')
    for trabalho in trabalhos.objects.all().iterator():
        tag = tags.objects.get(nome=trabalho.tag)
        trabalho.nova_tag = tag
        trabalho.save()


class Migration(migrations.Migration):

    dependencies = [
        ('trabalhos', '0007_auto_20180616_0055'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.RunPython(migrarTags),
        migrations.AddField(
            model_name='trabalho',
            name='nova_tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='trabalhos.Tag', null=True),
        ),
        migrations.RunPython(associarTags),
    ]