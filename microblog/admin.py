from django.contrib import admin

# Register your models here.
from microblog.models import HotSpot
#from microblog.models import Hot


@admin.register(HotSpot)
class SpotAdmin(admin.ModelAdmin):
    # 设置页面列的名称
    list_display = ['pk', 'content', 'author', 'publishTime', 'repost',
                    'comment', 'approve', 'address']
    list_per_page = 10

    ordering = ('pk',)

    search_fields = ['content']

    # 执行动作的位置
    actions_on_bottom = True
    actions_on_top = False
