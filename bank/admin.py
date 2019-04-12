from django.contrib import admin

# Register your models here.
from bank.models import Banks, Branches


@admin.register(Banks)
class BanksAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(Branches)
class BranchesAdmin(admin.ModelAdmin):
    list_display = (
        'ifsc', 'bank', 'branch',)
