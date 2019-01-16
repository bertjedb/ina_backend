# Generated by Django 2.0.5 on 2019-01-16 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ina_api', '0004_auto_20190116_1319'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ina_api.Project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ina_api.User')),
            ],
        ),
    ]
