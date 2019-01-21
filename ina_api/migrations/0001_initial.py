# Generated by Django 2.0.5 on 2019-01-19 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_uid', models.CharField(max_length=10, unique=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('desc', models.TextField(max_length=2000)),
                ('photo_path', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('member_count', models.IntegerField(default=0)),
                ('public', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Group_Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ina_api.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.TextField(max_length=3000)),
                ('start_date', models.DateTimeField(null=True)),
                ('end_date', models.DateTimeField(null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('like_count', models.IntegerField(default=0)),
                ('follower_count', models.IntegerField(default=0)),
                ('location', models.CharField(max_length=200)),
                ('thumbnail', models.CharField(default='no path', max_length=1000)),
                ('status', models.IntegerField(choices=[(0, 'New'), (1, 'OnGoing'), (2, 'Ended')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Project_Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ina_api.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Project_Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ina_api.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Project_Followed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ina_api.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Project_Liked',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ina_api.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Project_Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ina_api.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Project_Update',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=3000)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('thumbnail', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50, unique=True)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('bio', models.TextField(max_length=2000)),
                ('password', models.CharField(max_length=200)),
                ('salt', models.CharField(max_length=50, null=True)),
                ('mobile', models.CharField(max_length=22)),
                ('organisation', models.CharField(max_length=200)),
                ('function', models.CharField(max_length=200)),
                ('profile_photo_path', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('passwordVerification', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User_Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ina_api.Tag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ina_api.User')),
            ],
        ),
        migrations.AddField(
            model_name='project_update',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ina_api.User'),
        ),
        migrations.AddField(
            model_name='project_update',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ina_api.Project'),
        ),
        migrations.AddField(
            model_name='project_tag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ina_api.Tag'),
        ),
        migrations.AddField(
            model_name='project_liked',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ina_api.User'),
        ),
        migrations.AddField(
            model_name='project_followed',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ina_api.User'),
        ),
        migrations.AddField(
            model_name='project_favorite',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ina_api.User'),
        ),
        migrations.AddField(
            model_name='project_admin',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ina_api.User'),
        ),
        migrations.AddField(
            model_name='project',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ina_api.User'),
        ),
        migrations.AddField(
            model_name='member',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ina_api.Project'),
        ),
        migrations.AddField(
            model_name='member',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ina_api.User'),
        ),
        migrations.AddField(
            model_name='group_admin',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ina_api.User'),
        ),
        migrations.AddField(
            model_name='file',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ina_api.Project'),
        ),
        migrations.AddField(
            model_name='device',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ina_api.User'),
        ),
        migrations.AddField(
            model_name='chat',
            name='user1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user1', to='ina_api.User'),
        ),
        migrations.AddField(
            model_name='chat',
            name='user2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user2', to='ina_api.User'),
        ),
    ]
