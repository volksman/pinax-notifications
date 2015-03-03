from django.contrib import admin

from .conf import settings
from .models import NoticeType, NoticeQueueBatch


class NoticeTypeAdmin(admin.ModelAdmin):
    list_display = ["label", "display", "description", "default"]


class NoticeSettingAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "notice_type", "medium", "send"]


admin.site.register(NoticeQueueBatch)
admin.site.register(NoticeType, NoticeTypeAdmin)
admin.site.register(settings.PINAX_NOTIFICATIONS_GET_SETTING_MODEL(), NoticeSettingAdmin)
