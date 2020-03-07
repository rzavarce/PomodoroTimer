from django.contrib import admin

from .models import Task





class TasksAdmin(admin.ModelAdmin):

    list_display = ('tsk_title', 'tsk_config', 'tsk_status', 'tsk_assignted_time',)
    list_filter = ('tsk_title', 'tsk_status',)
    ordering = ('tsk_title',)
    search_fields = ('tsk_title',)    


    #fields = ['nickname', 'bike_category', 'bike_model', 'bike_serie', 'registration_number', 'manufacturing_year', 'manufacturer', 'engines_type', 'description', 'status', 'status_dry', 'client', 'device' ]

       		

admin.site.register(Task, TasksAdmin)




