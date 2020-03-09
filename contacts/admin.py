from django.contrib import admin

from .models import Contact





class ContacsAdmin(admin.ModelAdmin):

    list_display = ('cnt_name', 'cnt_email', 'cnt_message', 'cnt_status',)
    list_filter = ('cnt_name', 'cnt_email',)
    ordering = ('-id',)
    search_fields = ('cnt_name', 'cnt_email', )    



admin.site.register(Contact, ContacsAdmin)






