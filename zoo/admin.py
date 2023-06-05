from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Excursions, Account


class ExcursionAdmin(admin.ModelAdmin):
    list_filter = ('date', 'peopleAmount', 'guide', 'isFinished')
    list_display = ('date', 'time', 'phone', 'guide')


class GroupFilter(admin.SimpleListFilter):
    title = 'Group'
    parameter_name = 'group'

    def lookups(self, request, model_admin):
        return Group.objects.values_list('id', 'name')

    def queryset(self, request, queryset):
        group_id = self.value()
        if group_id:
            return queryset.filter(user__groups__id=group_id)
        return queryset


class AccountAdmin(admin.ModelAdmin):
    list_filter = (GroupFilter,)


admin.site.register(Excursions, ExcursionAdmin)
admin.site.register(Account, AccountAdmin)
