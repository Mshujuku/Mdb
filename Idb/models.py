from django.db import models

# Create your models here.

class Idb(models.Model):
    # 标题/名称 防止重复录入
    title = models.CharField(max_length=100,unique=True)
    # 地区[日本/韩国/欧美/国产/其他]
    country_choices = (
        (0,'国产'),
        (1,'日本'),   
        (2,'韩国'),
        (3,'欧美'),
        (4,'其他')
    )   
    country = models.IntegerField(choices=country_choices)  
    # 类型[动画/剧集/电影]
    genre_choices = (
        (0,'动画'),
        (1,'剧集'),   
        (2,'电影')
    )   
    genre = models.IntegerField(choices=genre_choices) 
    # 剧情简介
    summary = models.CharField(max_length=1000)
    # 分集
    episode = models.CharField(max_length=30)
    # 是否完结
    end_choices = (
        (0,'连载'),
        (1,'完结')
    )   
    end = models.IntegerField(choices=end_choices) 
    # 录入时间
    add_date = models.DateField(auto_now_add=True)
    # 字幕组
    subgroup = models.CharField(max_length=30)
    # 字幕组源地址
    subgroup_from = models.URLField()
    # 字幕组源地址
    subgroup_download = models.URLField()
    # M叔剧库里的阿里云盘链接
    mshuyunpan = models.URLField()
