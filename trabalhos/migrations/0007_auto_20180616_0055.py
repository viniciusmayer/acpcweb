# Generated by Django 2.0.6 on 2018-06-16 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trabalhos', '0006_auto_20180615_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabalho',
            name='natureza',
            field=models.CharField(default='OUTRA', max_length=255),
            preserve_default=False,
        ),
    ]
