# Generated by Django 2.0.5 on 2019-01-16 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ina_api', '0008_merge_20181221_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='thumbnail',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
