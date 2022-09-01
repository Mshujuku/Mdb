from django.contrib import admin
from .models import Idb


class IdbAdmin(admin.ModelAdmin):
    # 定制哪些字段需要展示
    list_display = ('id', 'title', 'country', 'genre', 'summary', 'episode', 'end', 'subgroup', 'subgroup_from', 'subgroup_download', 'mshuyunpan', 'add_date')
    # 定义哪个字段可以编辑
    #list_editable = ('title', 'country', 'genre', 'summary', 'episode', 'end', 'subgroup', 'subgroup_from', 'subgroup_download', 'mshuyunpan')
    # 默认title排序
    # list_display_links = ('title', ) 
    # sortable_by # 排序

    # 分页：每页10条
    # list_per_page = 5
    # 最大条目
    # list_max_show_all = 200

    # 搜索框 ^, =, @, None=icontains
    search_fields = ['title']
    # 过滤选项
    # list_filter = ('status', 'author__is_superuser', )

    # 按日期分组
    # date_hierarchy = 'create_date'
    # 默认空值
    # empty_value_display = 'NA'

 

admin.site.register(Idb, IdbAdmin)


