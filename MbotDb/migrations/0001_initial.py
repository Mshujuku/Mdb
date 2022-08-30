# Generated by Django 3.2.15 on 2022-08-30 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MbotDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg_id', models.CharField(max_length=100)),
                ('msg_time_rec', models.DateTimeField(auto_now_add=True)),
                ('msg_group_name', models.CharField(max_length=100)),
                ('msg_from_user', models.CharField(max_length=100)),
                ('msg_content', models.TextField()),
                ('msg_create_time', models.DateTimeField(auto_now_add=True)),
                ('msg_type', models.CharField(max_length=100)),
            ],
        ),
    ]
