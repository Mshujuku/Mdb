from django.contrib import admin
from .models import MbotDb

# Register your models here.

class MbotDbAdmin(admin.ModelAdmin):
    # 定制哪些字段需要展示
    list_display = ('id', 'msg_id', 'msg_time_rec', 'msg_group_name', 'msg_from_user', 'msg_content', 'msg_create_time', 'msg_type')

    # 默认title排序
    list_display_links = ('id', ) 
    # sortable_by # 排序
    # 定义哪个字段可以编辑
    # list_editable = ('status', )
    # 分页：每页10条
    # list_per_page = 5
    # 最大条目
    # list_max_show_all = 200

    # 搜索框 ^, =, @, None=icontains
    search_fields = ['msg_content']
    # 过滤选项
    # list_filter = ('status', 'author__is_superuser', )

    # 按日期分组
    # date_hierarchy = 'create_date'
    # 默认空值
    # empty_value_display = 'NA'

 

admin.site.register(MbotDb, MbotDbAdmin)








