# Generated by Django 3.2.15 on 2022-08-30 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Idb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('country', models.IntegerField(choices=[(0, '国产'), (1, '日本'), (2, '韩国'), (3, '欧美'), (4, '其他')])),
                ('genre', models.IntegerField(choices=[(0, '动画'), (1, '剧集'), (2, '电影')])),
                ('summary', models.CharField(max_length=1000)),
                ('episode', models.CharField(max_length=30)),
                ('end', models.IntegerField(choices=[(0, '连载'), (1, '完结')])),
                ('add_date', models.DateField(auto_now_add=True)),
                ('subgroup', models.CharField(max_length=30)),
                ('subgroup_from', models.URLField(default='a')),
                ('subgroup_download', models.URLField(default='a')),
                ('mshuyunpan', models.URLField(default='a')),
            ],
        ),
    ]
